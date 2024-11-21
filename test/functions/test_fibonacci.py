from hypothesis import given, strategies as st

from functions import fibonacci


@given(st.integers())
def test_fibonacci(n):
    assert fibonacci(n) >= 0
