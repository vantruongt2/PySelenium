from tests_trung.testcases.test_base import TestBase
from tests_trung.pages.login_page import LoginPage
from tests_trung.pages.dashboard_page import DashboardPage
import pytest
import logging
from tests_trung.data import aut_messages
from tests_trung.pages.general_page import GeneralPage
from tests_trung.utils import browser_helper, constants


class Test_login(TestBase):

    login_page = LoginPage()
    dashboard_page = DashboardPage()
    general_page = GeneralPage()

    testdata = [
        ("abc", "abc", aut_messages.INVALID_USER_OR_PASSWORD_WARN),
        ("administrator", "abc", aut_messages.INVALID_USER_OR_PASSWORD_WARN),
    ]

    @pytest.mark.usefixtures("clean_up_invalid_login")
    @pytest.mark.parametrize("da_user_name,da_password,alert_message", testdata)
    def test_da_invalid_login(self, da_user_name, da_password, alert_message):
        logging.info("1. Navigate TA Dashboard")
        self.login_page.go_to()

        logging.info("2. Logging with valid user")
        self.login_page.login(da_user_name, da_password)

        logging.info("Verify that warning message displays")
        assert alert_message in browser_helper.get_alert_text()

    @pytest.mark.usefixtures("clean_up_valid_login")
    def test_da_valid_login(self):
        logging.info("1. Navigate TA Dashboard")
        self.login_page.go_to()

        logging.info("2. Logging with valid user")
        self.login_page.login()

        logging.info("Verify user is able to log in successfully")
        assert constants.DEFAULT_PAGE_TITLE in browser_helper.get_title()

    @pytest.fixture()
    def clean_up_invalid_login(self):
        yield
        browser_helper.dismiss_alert()

    @pytest.fixture()
    def clean_up_valid_login(self):
        yield
        self.dashboard_page.logout()
