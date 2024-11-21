import functools


@functools.cache
def fibonacci(n: int) -> int:
    """
    Computes the nth number in the Fibonacci sequence.
    """
    assert n >= 0, f"n must be >= 0; {n} was passed."

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
