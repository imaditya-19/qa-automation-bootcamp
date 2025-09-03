import pytest

def factorial(n):
    """Compute the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
@pytest.mark.parametrize(
    "num,expected",
    [
        (0, 1), (1, 1), (2, 2), (3, 6),
        (4, 24), (5, 120), (6, 720),
        (7, 5040), (8, 40320), (9, 362880),
        (10, 3628800)
    ]
)
def test_factorial(num, expected):
    assert factorial(num) == expected

