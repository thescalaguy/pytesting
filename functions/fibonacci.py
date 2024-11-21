import functools


@functools.cache
def fibonacci(n: int) -> int:
    """
    Computes the nth number in the Fibonacci sequence.
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)
