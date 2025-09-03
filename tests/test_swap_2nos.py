
import pytest

@pytest.mark.parametrize("a, b", [(10, 20), (1, 2), (100, 200)])
def test_swap_tuple(a, b):
	orig_a, orig_b = a, b
	a, b = b, a
	assert a == orig_b and b == orig_a

@pytest.mark.parametrize("a, b", [(10, 20), (1, 2), (100, 200)])
def test_swap_temp(a, b):
	orig_a, orig_b = a, b
	temp = a
	a = b
	b = temp
	assert a == orig_b and b == orig_a