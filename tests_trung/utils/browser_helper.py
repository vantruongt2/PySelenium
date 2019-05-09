from selenpy.support import browser
import time
from selenium.webdriver.support.wait import WebDriverWait
import logging
from selenpy.common import config


def wait_for_page_loaded(timeout = None):
    if timeout is None:
        timeout = config.timeout
    page_status = browser.get_driver().execute_script('return document.readyState;')
    jquery_status = browser.get_driver().execute_script('return jQuery.active;')
    time_count = 0
    while not((page_status == "complete") and (jquery_status == 0)) and time_count < timeout:
        time.sleep(0.2)
        page_status = browser.get_driver().execute_script('return document.readyState;')
        jquery_status = browser.get_driver().execute_script('return jQuery.active;')
        time_count = time_count + 0.2


def wait_for_ajax(timeout = None):
    if timeout is None:
        timeout = config.timeout
    wait = WebDriverWait(browser.get_driver(), timeout)
    try:
        wait.until(lambda isjQueryActive: browser.get_driver().execute_script('return jQuery.active') == 0)
        wait.until(lambda isReady: browser.get_driver().execute_script('return document.readyState') == 'complete')
    except Exception as e:
        logging.info(e)


def dismiss_alert():
    browser.close_alert()


def get_alert_text():
    return browser.get_alert().text


def accept_alert():
    browser.get_alert().accept()
    wait_for_ajax()


def get_title():
    return browser.get_driver().title
