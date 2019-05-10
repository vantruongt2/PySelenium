from tests_thien.testcases.test_base import TestBase
from tests_thien.pages.dashboard.login_page import LoginPage
from tests_thien.pages.dashboard.dashboard_page import DashboardPage
from tests_thien.utilities import constant, browser_helper
import pytest
import logging

class LoginTest(TestBase):
    login_page = LoginPage()
    da_page = DashboardPage()

    @pytest.mark.usefixtures("clean_up_valid_login")
    def test_001_login_successful(self):
        logging.info("Verify that user can login specific repository successfully via Dashboard login page with correct credentials")
        self.login_page.login(constant.DA_USER,constant.DA_PWD)
        assert self.da_page.is_page_displayed(constant.MAIN_PAGE_TITLE)
    
    @pytest.mark.usefixtures("clean_up_invalid_login")
    def test_002_login_unsuccessful_with_valid_username_and_invalid_password(self):
        logging.info("Verify that user fails to log in specific repository successfully via Dashboard login page with correct username and incorrect password")         
        self.login_page.login(constant.DA_USER, constant.DA_INVALID_PWD, False)
        assert self.login_page.is_message_displayed(constant.MSG_LOGIN_FAIL)
    
    @pytest.mark.usefixtures("clean_up_invalid_login")
    def test_003_login_unsuccessful_with_invalid_username_password(self):
        logging.info("Verify that user fails to login specific repository successfully via Dashboard login page with incorrect credentials")
        self.login_page.login(constant.DA_INVALID_USER,constant.DA_INVALID_PWD, False)
        assert self.login_page.is_message_displayed(constant.MSG_LOGIN_FAIL)
    
    @pytest.fixture()
    def clean_up_valid_login(self):
        self.login_page.open()
        yield
        self.da_page.log_out()
    
    @pytest.fixture()
    def clean_up_invalid_login(self):
        yield
        browser_helper.dismiss_alert()
