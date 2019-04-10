import random
from string import ascii_letters

OUR_SERVICE_URL = 'http://ourservice.com/'


def get_short_url():
    short_url = ''.join(random.choices(ascii_letters, k=30))
    return short_url
