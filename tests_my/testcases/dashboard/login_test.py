from selenpy.support import browser
from tests_my.pages.dashboard.login_page import LoginPage
from tests_my.testcases.test_base import TestBase
from tests_my.testcases.utils import constants, common
import pytest
from tests_my.pages.dashboard.dashboard_page import DashboardPage
import logging

class Test_Login(TestBase):

    login_page = LoginPage()
    dashboard_page = DashboardPage()

    @pytest.fixture()
    def setup_class(self):
        yield
        self.dashboard_page.log_out()

    def test_login_001(self, setup_class):

        logging.info("Login with valid username and password")
        self.login_page.login(constants.USER_NAME, constants.PASSWORD)

        logging.info("Verify dashboad is displayed successfully")
        assert self.dashboard_page.is_At()

    testdata = [
        ("abc", "abc", constants.LOGIN_ERROR_MESSAGE),
        ("administrator", "abc", constants.LOGIN_ERROR_MESSAGE),
    ]

    @pytest.mark.parametrize("username,password,expected", testdata)
    def test_login_002(self, username, password, expected):

        logging.info("Login with invalid username: "+username+ " and password: "+password)
        self.login_page.login(username, password)

        logging.info("Verify error message is displayed")
        assert common.get_alert_text() == expected
        browser.close_alert()
