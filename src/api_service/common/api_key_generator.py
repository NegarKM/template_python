import hashlib
import random
import string

LENGTH = 40


def generate_api_key_secret() -> (str, str):
    """Generate a random API key of specified length."""
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=LENGTH))
    secret = hashlib.md5(key.encode()).hexdigest()
    return key, secret


# Generate a 32-character API key
# Generate the API secret using MD5 hexdigest of the API key
api_key, api_secret = generate_api_key_secret()
