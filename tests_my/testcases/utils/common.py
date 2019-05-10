import string
import random


def random_string(stringLength=10):
    letters = string.ascii_lowercase
    return '_' + ''.join(random.sample(letters, stringLength))
