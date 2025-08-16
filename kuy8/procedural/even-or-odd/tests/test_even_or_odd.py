from typing import Any

import pytest
from src.even_or_odd import even_or_odd


@pytest.mark.parametrize("value", [-2, 0, 2, 10**6])
def test_even_numbers(value: int) -> None:
    """Test that even numbers return 'Even'."""
    assert even_or_odd(value) == "Even"


@pytest.mark.parametrize("value", [-1, 1, 99, 10**6 + 1])
def test_odd_numbers(value: int) -> None:
    """Test that odd numbers return 'Odd'."""
    assert even_or_odd(value) == "Odd"


@pytest.mark.parametrize("value", ["string", 3.14, None, [1], {"num": 2}])
def test_invalid_input(value: Any) -> None:
    """Test that invalid input raises TypeError."""
    with pytest.raises(TypeError):
        even_or_odd(value)
