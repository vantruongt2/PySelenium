import unittest
import pytest

from selenpy.support import browser
from selenpy.support.conditions import have


class TestBase(unittest.TestCase):
    
    @pytest.fixture(scope="session", autouse=True)
    def setup(self):        
        browser.start_driver("chrome")
        browser.maximize_browser()
        browser.open_url("https://google.com")
        browser.wait_until(have.title("Google"))

        # Close all browsers when tests have been finished
        yield        
        browser.quit_all_browsers()        
