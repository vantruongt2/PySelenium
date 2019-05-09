import random
import string
from tests_phi.utils import evironment_variables


def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters,stringLength))
   

def get_url():
    return evironment_variables.da_url
