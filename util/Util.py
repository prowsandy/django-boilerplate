import string
import random
from django.core.signing import Signer
signer = Signer()

def random_string_generator(size=6, chars=string.ascii_uppercase + string.digits):
    str = ''.join(random.choice(chars) for _ in range(size - 1))
    return str

def unsign_key(key):
    return signer.unsign(key)