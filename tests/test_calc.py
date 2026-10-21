import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from calc import add, mul


def test_add():
    assert add(2, 3) == 5


def test_mul():
    assert mul(2, 3) == 6
