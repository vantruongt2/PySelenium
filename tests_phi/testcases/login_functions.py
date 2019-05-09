from tests_phi.testcases.test_base import TestBase
from tests_phi.pages.login_page import LoginPage
from tests_phi.pages.dashboard_page import DashboardPage
from tests_phi.utils import constants
from tests_phi.utils import browser_helper
import logging
import pytest

class Test_Login(TestBase):
    
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    
    @pytest.mark.usefixtures("clean_up_tc002")     
    def test_da_login_tc002(self):
        '''Verify that user fails to login specific repository successfully via Dashboard login page with incorrect credentials'''
        
        logging.info("1. Navigate to login page")
        self.login_page.go_to()
        
        logging.info("2. Login with invalid account")
        self.login_page.login(constants.USERNAME+"Incorrect", constants.INVALID_PASSWORD, False)
        
        logging.info("VP: '%s' message displays"% constants.INCORRECT_LOGIN_MESSAGE)
        assert browser_helper.get_alert_text() == constants.INCORRECT_LOGIN_MESSAGE
    
    @pytest.mark.usefixtures("clean_up_tc002")
    def test_da_login_tc003(self):
        '''Verify that user fails to log in specific repository successfully via Dashboard login page with correct username and incorrect password'''
        
        logging.info("1. Navigate to login page")
        self.login_page.go_to()
        
        logging.info("2. Login with invalid account")
        self.login_page.login(constants.USERNAME, constants.INVALID_PASSWORD, False)
        
        logging.info("VP: '%s' message displays"% constants.INCORRECT_LOGIN_MESSAGE)
        assert browser_helper.get_alert_text() == constants.INCORRECT_LOGIN_MESSAGE
    
    @pytest.mark.usefixtures("clean_up_tc001")
    def test_da_login_tc001(self):
        '''Verify that user can login specific repository successfully via Dashboard login page with correct credentials'''
        
        logging.info("1. Navigate to login page")
        self.login_page.go_to()
         
        logging.info("2. Login with valid account")
        self.login_page.login(constants.USERNAME, constants.VALID_PASSWORD)
         
        logging.info("VP: Dashboard page displays")
        assert "Execution Dashboard" in browser_helper.get_page_title()
        
    @pytest.fixture()
    def clean_up_tc002(self):
        yield
        logging.info("Teardown: Dismiss alert")
        browser_helper.dismiss_alert()
        
    @pytest.fixture()
    def clean_up_tc001(self):
        yield
        logging.info("Teardown: Logout")
        self.dashboard_page.logout()
