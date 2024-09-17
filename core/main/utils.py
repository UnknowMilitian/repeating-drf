import random
import string
import base64
from django.conf import settings


def create_basic_authentication_header(phone, password):
    value = f"{phone}:{password}"
    encoded_value = base64.b64encode(value.encode()).decode()
    return f"Basic {encoded_value}"


def generate_code():
    return "".join(random.choices(string.digits, k=6))
