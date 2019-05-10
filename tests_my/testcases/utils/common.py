import string
import random
from selenpy.support import browser
from selenium.webdriver.support.wait import WebDriverWait
from tests_my.testcases.utils import constants


def random_string(stringLength=10):
    letters = string.ascii_lowercase
    return '_' + ''.join(random.sample(letters, stringLength))\
