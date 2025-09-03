import pytest

def is_prime(n):
    """Check if a number is prime."""
    try:
        if n < 2:
            return False
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        return count == 2  # Returns True if prime, False otherwise
    except TypeError:
        raise ValueError("Input must be a non-negative integer")
    
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
        (37, True), (100, False),(150, False),
        (97, True), (89, True), (77, False), (49, False),
        (3.5, ValueError), ("a", ValueError), (None, ValueError), ([], ValueError)  
            

    ]
)
def test_is_prime(num, expected):
        if expected == ValueError:
            with pytest.raises(ValueError):
                is_prime(num)
        else:
            assert is_prime(num) == expected

if __name__ == "__main__":
    interactive_check()