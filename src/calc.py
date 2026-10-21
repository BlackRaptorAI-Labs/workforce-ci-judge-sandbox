def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def safe_div(a, b):
    """a / b, or None when b is 0."""
    if b == 0:
        return None
    return a / b
