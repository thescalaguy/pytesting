import functools


@functools.cache
def fibonacci(n: int) -> int:
    """
    Computes the nth number in the Fibonacci sequence.
    """
    assert 0 <= n <= 300, f"n must be between 0 and 300; {n} was passed."

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
