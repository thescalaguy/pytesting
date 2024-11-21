import pytest
from hypothesis import given, strategies as st, example

from functions import fibonacci


@given(st.integers(min_value=0, max_value=10))
def test_fibonacci(n):
    assert fibonacci(n) >= 0


@given(st.integers(min_value=-2, max_value=-1))
def test_fibonacci(n):
    with pytest.raises(AssertionError):
        fibonacci(n)
