
from selenpy.support import factory
from selenpy.common import config
from selenpy.helper.wait import wait_for
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


def get_driver():
    return factory.get_shared_driver()


def maximize_browser():
    get_driver().maximize_window()

        
def open_url(url):
    get_driver().get(url)    


def switch_to_driver(driver_key="default"):
    factory.switch_to_driver(driver_key)


def close_browser():
    factory.close_browser()


def quit_all_browsers():
    factory.quit_all_browsers()


def start_driver(name, remote_host, key="default"):
    factory.start_driver(name, remote_host, key)


def wait_until(webdriver_condition, timeout=None, polling=None):
    if timeout is None:
        timeout = config.timeout
    if polling is None:
        polling = config.poll_during_waits

    return wait_for(get_driver(), webdriver_condition, timeout, polling)


def switch_to_alert():
    try:
        WebDriverWait(get_driver(), 5).until(EC.alert_is_present(), 'Timed out waiting for alerts to appear')
        return get_driver().switch_to.alert
    except TimeoutException:
        logging.info("no alert")


def close_alert():
    switch_to_alert().dismiss()


def move_to_element(element):
    ActionChains(get_driver()).move_to_element(element).perform()
