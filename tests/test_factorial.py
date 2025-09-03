import pytest

def factorial(n):
    """Compute the factorial of a number."""
    try:

        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    except TypeError:
        raise ValueError("Input must be a non-negative integer")
    
@pytest.mark.parametrize(
    "num,expected",
    [
        (0, 1), (1, 1), (2, 2),
        (4, 24), (5, 120), (6, 720),
        (7, 5040), (8, 40320),
        (10, 3628800), (12, 479001600),(-1, ValueError),
        (3.5, ValueError), ("a", ValueError),(20, 2432902008176640000),(None, ValueError), ([], ValueError)

    ]
)
def test_factorial(num, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            factorial(num)
    else:
        assert factorial(num) == expected

