"""Offline tests for the restored stock-symbol/current-price adapter."""

import pytest

from core.market_data import fetch_current_price


class _ILoc:
    def __getitem__(self, index):
        assert index == -1
        return 214.187


class _Closes:
    empty = False
    iloc = _ILoc()

    def dropna(self):
        return self


class _History:
    def __getitem__(self, key):
        assert key == "Close"
        return _Closes()


class _Ticker:
    def history(self, period):
        assert period == "5d"
        return _History()


def _ticker_factory(symbol):
    assert symbol == "IBM"
    return _Ticker()


def test_fetch_current_price_normalizes_symbol_and_rounds_price():
    symbol, price = fetch_current_price(" ibm ", ticker_factory=_ticker_factory)
    assert symbol == "IBM"
    assert price == 214.19


def test_fetch_current_price_rejects_blank_symbol():
    with pytest.raises(ValueError, match="required"):
        fetch_current_price("   ", ticker_factory=_ticker_factory)


def test_fetch_current_price_wraps_provider_failure():
    def failing_factory(_symbol):
        raise ConnectionError("offline")

    with pytest.raises(RuntimeError, match="Unable to load"):
        fetch_current_price("TSLA", ticker_factory=failing_factory)
