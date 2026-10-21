import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from calc import add


def test_add():
    assert add(2, 3) == 5
