import pytest

from selenpy.support import browser
import logging
from tests_my.testcases.utils import environment


class TestBase():

    @pytest.fixture(scope="session", autouse=True)
    def setup(self):
        logging.info("Starting the test on " + str(pytest.browser_name))                
        browser.start_driver(pytest.browser_name, pytest.remote_host)
        browser.maximize_browser()
        browser.open_url(environment.dashboard_url)
        # Close all browsers when tests have been finished
        yield
        browser.quit_all_browsers()
