import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from calc import safe_div


def test_runs():
    safe_div(6, 3)
