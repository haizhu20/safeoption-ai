"""Current stock-price lookup for SafeOption AI.

This module intentionally restores only the verified v1 behavior:
stock symbol -> latest available closing price.  It does not claim to
provide a live option chain, option premiums, IV, volume, or open interest.
"""


def fetch_current_price(symbol, ticker_factory=None):
    """Return ``(normalized_symbol, latest_close)``.

    ``ticker_factory`` is injectable so the behavior can be unit-tested
    without network access.
    """
    normalized = str(symbol or "").strip().upper()
    if not normalized:
        raise ValueError("Stock symbol is required.")

    if ticker_factory is None:
        import yfinance as yf

        ticker_factory = yf.Ticker

    try:
        history = ticker_factory(normalized).history(period="5d")
        closes = history["Close"].dropna()
        if closes.empty:
            raise ValueError("No closing-price data returned.")
        price = float(closes.iloc[-1])
    except Exception as exc:
        raise RuntimeError(
            f"Unable to load a current price for {normalized}."
        ) from exc

    if price <= 0:
        raise RuntimeError(f"Invalid market price returned for {normalized}.")

    return normalized, round(price, 2)
