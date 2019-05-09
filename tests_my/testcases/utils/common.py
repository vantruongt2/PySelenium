import string
import random
from selenpy.support import browser
from selenium.webdriver.support.wait import WebDriverWait
from tests_my.testcases.utils import constants


def random_string(stringLength=10):
    letters = string.ascii_lowercase
    return '_' + ''.join(random.sample(letters, stringLength))


def get_title():
    return browser.get_driver().title


def get_alert_text():
    alert = browser.get_alert()
    return alert.text


def accept_alert():
    browser.get_alert().accept()


def wait_for_page_loaded():
    WebDriverWait(browser.get_driver(), constants.WAIT_CONDITION_TIME).until(lambda d: d.execute_script("return jQuery.active == 0"))
