from tests_my.pages.dashboard.login_page import LoginPage
from tests_my.testcases.test_base import TestBase
from tests_my.testcases.utils import constants, browser_helper
import pytest
from tests_my.pages.dashboard.dashboard_page import DashboardPage
import logging


class Test_Login(TestBase):

    login_page = LoginPage()
    dashboard_page = DashboardPage()

    testdata = [
        ("abc", "abc", constants.LOGIN_ERROR_MESSAGE),
        ("administrator", "abc", constants.LOGIN_ERROR_MESSAGE),
    ]

    def test_login_001(self, clean_up_001):

        logging.info("Login with valid username and password")
        self.login_page.login(constants.USER_NAME, constants.PASSWORD)

        logging.info("Verify dashboad is displayed successfully")
        assert self.dashboard_page.is_at()

    @pytest.mark.parametrize("username,password,expected", testdata)
    def test_login_002(self, username, password, expected, clean_up_002):

        logging.info("Login with invalid username: " + username + " and password: " + password)
        self.login_page.login(username, password)

        logging.info("Verify error message is displayed")
        assert browser_helper.get_alert_text() == expected

    @pytest.fixture()
    def clean_up_001(self):
        yield
        self.dashboard_page.log_out()

    @pytest.fixture()
    def clean_up_002(self):
        yield
        browser_helper.dismiss_alert()
