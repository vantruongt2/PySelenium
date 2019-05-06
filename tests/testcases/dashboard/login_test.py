from tests.testcases.test_base import TestBase
from tests.pages.dashboard.login_page import LoginPage
from tests.pages.dashboard.home_page import HomePage
from selenpy.support import browser
from tests.utils import constants
from ddt import data, unpack, ddt


@ddt
class LoginTest(TestBase):
    
    login_page = LoginPage()
    home_page = HomePage()
    
    def test_login_001(self):
        self.login_page.login(constants.USER_NAME, constants.PASSWORD)
        assert self.home_page.is_At() == True
        self.home_page.log_out()

    @data(('abc', 'abc'), ('administrator', 'abc'))
    @unpack
    def test_login_002(self, username, password):
        self.login_page.login(username, password)
        assert self.login_page.get_error_message() == constants.LOGIN_ERROR_MESSAGE
        browser.close_alert()
