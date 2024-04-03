"""Functions that implement sorting algorithms."""

__author__ = "730466512"

#  part one a and b.


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    for c in range(1, len(x)):
        current: int = x[c]
        d: int = c - 1 
        while d >= 0 and current < x[d]:
            x[d + 1] = x[d]
            d -= 1
        x[d + 1] = current


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    for a in range(len(x)):
        min_idx = a
        for b in range(a + 1, len(x)):
            if x[b] < x[min_idx]:
                min_idx = b
        if min_idx != a:
            temp: int = x[a]
            x[a] = x[min_idx]
            x[min_idx] = temp