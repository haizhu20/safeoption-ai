"""
SafeOption AI v3.1.2 - Option Chain Module
===========================================
v3.1 BASELINE — preserved.
PATCHED: FIX #2 — simulation_mode parameter added to validate_strike
"""

from datetime import datetime, timedelta


def generate_expiration_date(dte):
    exp_date = datetime.now() + timedelta(days=dte)
    return exp_date.strftime('%Y-%m-%d')


def generate_strike_chain(underlying_price, num_strikes=11, spacing=None):
    if spacing is None:
        if underlying_price < 25:
            spacing = 1.0
        elif underlying_price < 100:
            spacing = 2.5
        elif underlying_price < 300:
            spacing = 5.0
        elif underlying_price < 1000:
            spacing = 5.0
        else:
            spacing = 10.0
    center = round(underlying_price / spacing) * spacing
    half = num_strikes // 2
    strikes = [round(center + (i - half) * spacing, 2) for i in range(num_strikes)]
    return sorted([s for s in strikes if s > 0])


# ── FIX #2 PATCH: Added simulation_mode parameter ─────────────────────
def validate_strike(strike, underlying_price, simulation_mode=False):
    """
    Validate strike price.

    simulation_mode=False (default): standard chain validation
    simulation_mode=True:  accept arbitrary positive values within bounds
    """
    if strike <= 0:
        return False, "Strike price must be positive"

    if simulation_mode:
        # PATCH FIX #2: In simulation mode accept any reasonable positive strike
        if strike > underlying_price * 10:
            return False, "Strike exceeds 10x underlying"
        if strike < underlying_price * 0.01:
            return False, "Strike below 1% of underlying"
        return True, "Valid — simulation mode"

    # Live mode
    if strike > underlying_price * 5:
        return False, "Strike unreasonably high"
    if strike < underlying_price * 0.1:
        return False, "Strike unreasonably low"
    return True, "Valid"
# ── END FIX #2 ─────────────────────────────────────────────────────────


def get_dte_presets():
    return [7, 14, 30, 45, 60]
