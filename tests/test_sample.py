import pytest
from utils.helpers import get_timestamp, generate_random_string

def test_timestamp_format():
    ts = get_timestamp()
    assert "_" in ts
    assert len(ts) > 10

def test_random_string_length():
    s = generate_random_string(10)
    assert len(s) == 10
    assert s.isalnum()
