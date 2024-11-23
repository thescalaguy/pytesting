import pytest
from hypothesis import given, strategies as st

from functions import fibonacci


@given(st.integers(min_value=0, max_value=300))
def test_fibonacci(n):
    assert fibonacci(n) >= 0


@given(st.integers(min_value=5000))
def test_fibonacci_large_n(n):
    with pytest.raises(AssertionError):
        fibonacci(n)


@given(st.integers(min_value=-2, max_value=-1))
def test_fibonacci_negative(n):
    with pytest.raises(AssertionError):
        fibonacci(n)
