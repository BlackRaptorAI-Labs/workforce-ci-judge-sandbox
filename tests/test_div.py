import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from calc import safe_div


def test_divides():
    assert safe_div(6, 3) == 2


def test_fraction():
    assert safe_div(1, 4) == 0.25


def test_negative():
    assert safe_div(-6, 3) == -2


def test_zero_divisor_returns_none():
    assert safe_div(5, 0) is None


def test_zero_dividend():
    assert safe_div(0, 5) == 0
