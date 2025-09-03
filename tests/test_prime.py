import pytest

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count == 2  # Returns True if prime, False otherwise

# --- Interactive check ---
def interactive_check():
    try:
        num = int(input("Enter a number to check if it's prime: "))
        if is_prime(num):
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")
    except ValueError:
        print("Please enter a valid integer.")

# --- Pytest tests ---
@pytest.mark.parametrize(
    "num,expected",
    [
        (2, True), (3, True), (4, False), (5, True),
        (10, False), (13, True), (17, True),
        (23, True), (24, False), (1, False), (0, False),
        (-5, False), (29, True), (30, False), (31, True),
        (37, True), (100, False)
    ]
)
def test_is_prime(num, expected):
    assert is_prime(num) == expected

if __name__ == "__main__":
    interactive_check()