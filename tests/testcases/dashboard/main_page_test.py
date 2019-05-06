from tests.testcases.test_base import TestBase
from tests.pages.dashboard.login_page import LoginPage
from tests.pages.dashboard.home_page import HomePage
from tests.utils import constants

class LoginTest(TestBase):
    
    login_page = LoginPage()
    home_page = HomePage()
    
    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()
        cls.login_page.login(constants.USER_NAME, constants.PASSWORD)
        
    @classmethod
    def tearDownClass(cls):
        super(LoginTest, cls).tearDownClass()
        cls.home_page.log_out()
    
    def test_main_page_021(self):
        pass
