import datetime
import random
import string

def get_timestamp():
    """Return current timestamp in YYYY-MM-DD_HH-MM-SS format"""
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def generate_random_string(length=8):
    """Return random alphanumeric string"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
