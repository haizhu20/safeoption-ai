"""
SafeOption AI v3.1.2 - Risk Calculation Engine
================================================
Black-Scholes pricing, Greeks, risk classification,
probability of profit, and full position analysis.

v3.1 baseline — NO structural changes. Patched only where noted.
"""

import math


def _norm_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def _norm_pdf(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    if T <= 0:
        return max(S - K, 0.0) if option_type == 'call' else max(K - S, 0.0)
    sigma = max(sigma, 1e-6)
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    if option_type == 'call':
        price = S * _norm_cdf(d1) - K * math.exp(-r * T) * _norm_cdf(d2)
    else:
        price = K * math.exp(-r * T) * _norm_cdf(-d2) - S * _norm_cdf(-d1)
    return round(max(price, 0.0), 4)


def calculate_greeks(S, K, T, r, sigma, option_type='call'):
    if T <= 0:
        return {'delta': 0.0, 'gamma': 0.0, 'theta': 0.0, 'vega': 0.0, 'rho': 0.0}
    sigma = max(sigma, 1e-6)
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    nd1 = _norm_cdf(d1)
    pd1 = _norm_pdf(d1)
    gamma = pd1 / (S * sigma * math.sqrt(T))
    vega = S * pd1 * math.sqrt(T) / 100.0
    if option_type == 'call':
        delta = nd1
        theta = (-(S * pd1 * sigma) / (2.0 * math.sqrt(T))
                 - r * K * math.exp(-r * T) * _norm_cdf(d2)) / 365.0
        rho = K * T * math.exp(-r * T) * _norm_cdf(d2) / 100.0
    else:
        delta = nd1 - 1.0
        theta = (-(S * pd1 * sigma) / (2.0 * math.sqrt(T))
                 + r * K * math.exp(-r * T) * _norm_cdf(-d2)) / 365.0
        rho = -K * T * math.exp(-r * T) * _norm_cdf(-d2) / 100.0
    return {
        'delta': round(delta, 4), 'gamma': round(gamma, 6),
        'theta': round(theta, 4), 'vega': round(vega, 4), 'rho': round(rho, 4),
    }


def classify_risk(S, K, T, sigma):
    moneyness = K / S if S > 0 else 1.0
    dte = T * 365.0
    score = 0
    if 0.95 <= moneyness <= 1.05:
        score += 3
    elif moneyness < 0.90 or moneyness > 1.10:
        score += 1
    else:
        score += 2
    if dte <= 7:
        score += 3
    elif dte <= 21:
        score += 2
    else:
        score += 1
    if sigma >= 0.50:
        score += 3
    elif sigma >= 0.30:
        score += 2
    else:
        score += 1
    if score <= 3:
        return 'LOW'
    elif score <= 5:
        return 'MEDIUM'
    elif score <= 7:
        return 'HIGH'
    else:
        return 'VERY HIGH'


def estimate_probability_of_profit(S, K, T, r, sigma, option_type, position):
    if T <= 0 or sigma <= 0:
        return 0.0
    premium = black_scholes_price(S, K, T, r, sigma, option_type)
    breakeven = (K + premium) if option_type == 'call' else (K - premium)
    if breakeven <= 0:
        return 99.9
    sigma_eff = max(sigma, 1e-6)
    d2 = (math.log(S / breakeven) + (r - 0.5 * sigma_eff ** 2) * T) / (
        sigma_eff * math.sqrt(T))
    prob_above = _norm_cdf(d2) * 100.0
    if option_type == 'call':
        prob = prob_above if position == 'long' else 100.0 - prob_above
    else:
        prob = 100.0 - prob_above if position == 'long' else prob_above
    return round(max(min(prob, 99.9), 0.1), 1)


def position_analysis(S, K, T, r, sigma, option_type, position='long', contracts=1):
    price = black_scholes_price(S, K, T, r, sigma, option_type)
    greeks = calculate_greeks(S, K, T, r, sigma, option_type)
    multiplier = contracts * 100
    result = {
        'option_price': round(price, 2), 'greeks': greeks, 'breakeven': 0.0,
        'risk_level': classify_risk(S, K, T, sigma),
        'probability_of_profit': estimate_probability_of_profit(
            S, K, T, r, sigma, option_type, position),
        'contracts': contracts, 'multiplier': multiplier,
    }
    if option_type == 'call':
        if position == 'long':
            result['max_profit'] = 'Unlimited'
            result['max_loss'] = round(price * multiplier, 2)
            result['breakeven'] = round(K + price, 2)
            result['capital_required'] = round(price * multiplier, 2)
        else:
            result['max_profit'] = round(price * multiplier, 2)
            result['max_loss'] = 'Unlimited'
            result['breakeven'] = round(K + price, 2)
            result['capital_required'] = round(K * multiplier, 2)
    else:
        if position == 'long':
            result['max_profit'] = round(max((K - price) * multiplier, 0), 2)
            result['max_loss'] = round(price * multiplier, 2)
            result['breakeven'] = round(max(K - price, 0), 2)
            result['capital_required'] = round(price * multiplier, 2)
        else:
            result['max_profit'] = round(price * multiplier, 2)
            result['max_loss'] = round(max((K - price) * multiplier, 0), 2)
            result['breakeven'] = round(max(K - price, 0), 2)
            result['capital_required'] = round(K * multiplier, 2)
    return result
