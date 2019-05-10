
from selenpy.support import factory
from selenpy.common import config
from selenpy.helper.wait import wait_for
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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

    
def select_main_window():
    handles = get_driver().window_handles
    get_driver().switch_to.window(handles[0])


def wait_until(webdriver_condition, timeout=None, polling=None):
    if timeout is None:
        timeout = config.timeout
    if polling is None:
        polling = config.poll_during_waits

    return wait_for(get_driver(), webdriver_condition, timeout, polling)


def get_alert():
    try:
        WebDriverWait(get_driver(), config.timeout).until(EC.alert_is_present())
        return get_driver().switch_to.alert
    except TimeoutException:
        logging.info("No  alert")
        return None


def close_alert():
    if get_alert() is not None:
        get_alert().dismiss()
