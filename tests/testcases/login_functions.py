from tests.testcases.test_base import TestBase
from tests.pages.general_page import GeneralPage
from tests.pages.login_page import LoginPage
from tests.pages.dashboard_page import DashboardPage
from tests.utils import constants


class LoginTest(TestBase, GeneralPage):
    
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    
    incorrect_login_message = "Username or password is invalid"
    
    
    def test_da_login_tc001(self):
        self.login_page.go_to_login_page()
        self.login_page.login(constants.USERNAME,"")
        assert self.is_title_contains("Execution Dashboard")
        self.dashboard_page.logout()
         
 
    def test_da_login_tc002(self):
        self.login_page.go_to_login_page()
        self.login_page.login(constants.USERNAME+"Incorrect","abc")
        assert self.get_alert_text() == self.incorrect_login_message
        self.dismiss_alert()
 

    def test_da_login_tc003(self):
        self.login_page.go_to_login_page()
        self.login_page.login(constants.USERNAME,"abc")
        assert self.get_alert_text() == self.incorrect_login_message
        self.dismiss_alert()
