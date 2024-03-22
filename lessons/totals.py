"""Summing the elements of a list using different loops."""

__author__ = "730466512"


def w_sum(vals: list[float]) -> float:
    """Sum using while."""
    index: int = 0
    total: float = 0.0
    while index < len(vals):
        total += vals[index]
        index += 1 
    return total


a: list[float] = [1.0, 2.0, 3.0]
print(w_sum(a))


def f_sum(vals: list[float]) -> float:
    """Sums input values."""
    total: float = 0.0
    for elem in vals:
        total += elem 
    return total


def f_range_sum(vals: list[float]) -> float:
    """Same but using for in range loop."""
    total: float = 0.0
    for elem in range(len(vals)):
        total += vals[elem]
    return total