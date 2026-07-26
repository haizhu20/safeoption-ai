"""
SafeOption AI v3.1.2 - Test Suite
===================================
BASE:  v3.1 tests
PATCH: Tests for FIX #1 (DTE linkage) and FIX #2 (Simulation strikes)
"""

import sys, os, math, pytest
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from core.risk_engine import (
    black_scholes_price, calculate_greeks, classify_risk,
    estimate_probability_of_profit, position_analysis,
)
from core.option_chain import (
    generate_strike_chain, generate_expiration_date,
    validate_strike, get_dte_presets,
)
from ui.bilingual import get_text, TEXTS


class TestBlackScholes:
    def test_atm_call(self):
        assert 2 < black_scholes_price(260, 260, 30/365, 0.05, 0.25, 'call') < 20

    def test_atm_put(self):
        assert black_scholes_price(260, 260, 30/365, 0.05, 0.25, 'put') > 0

    def test_put_call_parity(self):
        S, K, T, r, v = 260, 260, 30/365, 0.05, 0.25
        c = black_scholes_price(S, K, T, r, v, 'call')
        p = black_scholes_price(S, K, T, r, v, 'put')
        assert abs((c - p) - (S - K * math.exp(-r * T))) < 0.01

    def test_deep_otm(self):
        assert black_scholes_price(260, 400, 7/365, 0.05, 0.25, 'call') < 0.05

    def test_expired_itm(self):
        assert black_scholes_price(270, 260, 0, 0.05, 0.25, 'call') == pytest.approx(10)
        assert black_scholes_price(250, 260, 0, 0.05, 0.25, 'put') == pytest.approx(10)

    def test_expired_otm(self):
        assert black_scholes_price(260, 270, 0, 0.05, 0.25, 'call') == 0
        assert black_scholes_price(260, 250, 0, 0.05, 0.25, 'put') == 0

    def test_vol_sensitivity(self):
        lo = black_scholes_price(260, 260, 30/365, 0.05, 0.15, 'call')
        hi = black_scholes_price(260, 260, 30/365, 0.05, 0.40, 'call')
        assert hi > lo


class TestGreeks:
    def test_call_delta(self):
        g = calculate_greeks(260, 260, 30/365, 0.05, 0.25, 'call')
        assert 0 < g['delta'] < 1

    def test_put_delta(self):
        g = calculate_greeks(260, 260, 30/365, 0.05, 0.25, 'put')
        assert -1 < g['delta'] < 0

    def test_gamma_positive(self):
        assert calculate_greeks(260, 260, 30/365, 0.05, 0.25, 'call')['gamma'] > 0

    def test_vega_positive(self):
        for ot in ['call', 'put']:
            assert calculate_greeks(260, 260, 30/365, 0.05, 0.25, ot)['vega'] > 0

    def test_theta_negative(self):
        assert calculate_greeks(260, 260, 30/365, 0.05, 0.25, 'call')['theta'] < 0

    def test_expired_zero(self):
        g = calculate_greeks(260, 260, 0, 0.05, 0.25, 'call')
        assert g['delta'] == 0 and g['gamma'] == 0

    def test_deep_itm_delta(self):
        assert calculate_greeks(260, 200, 60/365, 0.05, 0.25, 'call')['delta'] > 0.9


class TestRisk:
    def test_low(self):
        assert classify_risk(260, 220, 60/365, 0.15) == 'LOW'

    def test_range(self):
        for S, K, d, v in [(260,240,45,0.2),(260,260,7,0.35),(100,100,30,0.6)]:
            assert classify_risk(S, K, d/365, v) in ['LOW','MEDIUM','HIGH','VERY HIGH']


class TestProbability:
    def test_otm_short_put(self):
        assert estimate_probability_of_profit(260, 240, 30/365, 0.05, 0.25, 'put', 'short') > 50

    def test_otm_long_call(self):
        assert estimate_probability_of_profit(260, 280, 30/365, 0.05, 0.25, 'call', 'long') < 50

    def test_bounds(self):
        for ot in ['call', 'put']:
            for pos in ['long', 'short']:
                p = estimate_probability_of_profit(260, 260, 30/365, 0.05, 0.25, ot, pos)
                assert 0 < p < 100


class TestChain:
    def test_sorted(self):
        s = generate_strike_chain(260)
        assert s == sorted(s) and any(abs(x-260)<10 for x in s)

    def test_length(self):
        assert len(generate_strike_chain(260)) == 11

    def test_exp_future(self):
        assert datetime.strptime(generate_expiration_date(30), '%Y-%m-%d') > datetime.now()

    def test_presets(self):
        assert get_dte_presets() == [7, 14, 30, 45, 60]


class TestValidateStrike:
    def test_live_valid(self):
        assert validate_strike(260, 260)[0]

    def test_live_negative(self):
        assert not validate_strike(-10, 260)[0]

    def test_live_zero(self):
        assert not validate_strike(0, 260)[0]


# ── FIX #2 PATCH TESTS ────────────────────────────────────────────────

class TestSimulationPatch:
    def test_261(self):
        assert validate_strike(261, 260, simulation_mode=True)[0]

    def test_262_5(self):
        assert validate_strike(262.5, 260, simulation_mode=True)[0]

    def test_257(self):
        assert validate_strike(257, 260, simulation_mode=True)[0]

    def test_401(self):
        assert validate_strike(401, 260, simulation_mode=True)[0]

    def test_fractional(self):
        for s in [260.5, 261.25, 259.75]:
            assert validate_strike(s, 260, simulation_mode=True)[0]

    def test_analysis_valid(self):
        for s in [261, 262.5, 257, 401]:
            r = position_analysis(260, s, 30/365, 0.05, 0.25, 'put', 'short', 1)
            assert r['option_price'] >= 0
            assert r['risk_level'] in ['LOW','MEDIUM','HIGH','VERY HIGH']

    def test_extreme_rejected(self):
        assert not validate_strike(3000, 260, simulation_mode=True)[0]


# ── FIX #1 PATCH TESTS ────────────────────────────────────────────────

class TestDTELinkagePatch:
    def test_all_presets_valid(self):
        for dte in get_dte_presets():
            r = position_analysis(260, 260, dte/365, 0.05, 0.25, 'put', 'short', 1)
            assert r['option_price'] > 0

    def test_theta_relationship(self):
        t7 = abs(calculate_greeks(260, 260, 7/365, 0.05, 0.25, 'put')['theta'])
        t60 = abs(calculate_greeks(260, 260, 60/365, 0.05, 0.25, 'put')['theta'])
        assert t7 > t60

    def test_exp_matches_dte(self):
        for dte in get_dte_presets():
            d = datetime.strptime(generate_expiration_date(dte), '%Y-%m-%d').date()
            assert abs((d - datetime.now().date()).days - dte) <= 1


class TestBilingual:
    def test_en(self):
        assert get_text('English', 'app_title') == 'SafeOption AI'

    def test_cn(self):
        assert get_text('中文', 'app_title') == 'SafeOption AI'

    def test_parity(self):
        assert set(TEXTS['English'].keys()) == set(TEXTS['中文'].keys())

    def test_no_empty(self):
        for lang in ['English', '中文']:
            for k, v in TEXTS[lang].items():
                assert isinstance(v, str) and len(v) > 0


class TestAnalysis:
    def test_sell_put(self):
        r = position_analysis(260, 250, 30/365, 0.05, 0.25, 'put', 'short', 1)
        assert r['option_price'] > 0
        assert r['max_profit'] > 0
        assert r['breakeven'] < 250
        assert r['capital_required'] == 25000

    def test_buy_call(self):
        r = position_analysis(260, 270, 30/365, 0.05, 0.25, 'call', 'long', 1)
        assert r['max_profit'] == 'Unlimited'
        assert r['breakeven'] > 270

    def test_scale(self):
        s = position_analysis(260, 260, 30/365, 0.05, 0.25, 'put', 'short', 1)
        t = position_analysis(260, 260, 30/365, 0.05, 0.25, 'put', 'short', 3)
        assert t['max_profit'] == pytest.approx(s['max_profit'] * 3)

    def test_greeks_present(self):
        r = position_analysis(260, 260, 30/365, 0.05, 0.25, 'call', 'long', 1)
        assert all(k in r['greeks'] for k in ['delta','gamma','theta','vega','rho'])

    def test_expired(self):
        assert position_analysis(270, 260, 0, 0.05, 0.25, 'call', 'long', 1)['option_price'] == 10
