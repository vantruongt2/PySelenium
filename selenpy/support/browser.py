import os

from selenpy.support import factory


def maximize_browser():
    driver().maximize_window()

        
def open_url(url):
    driver().get(url)    


def switch_to_driver(driver_key="default"):
    factory.switch_to_driver(driver_key)


def close_browser():
    factory.close_browser()


def quit_all_browsers():
    factory.quit_all_browsers()


def start_driver(name):
    factory.start_driver(name)


def driver():
    return factory.get_shared_driver()

def wait_until(webdriver_condition, timeout=None, polling=None):
    if timeout is None:
        timeout = selene.config.timeout
    if polling is None:
        polling = selene.config.poll_during_waits

    return wait_for(driver(), webdriver_condition, timeout, polling)