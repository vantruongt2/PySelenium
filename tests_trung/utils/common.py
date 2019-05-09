from tests_trung.utils import constants
import datetime
import random
import string


def get_today(dt_format=constants.DATE_FORMAT):
    now = datetime.datetime.now()
    return now.strftime(dt_format)


def random_string(prefix="Prefix", stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return prefix + ''.join(random.sample(letters, stringLength))
