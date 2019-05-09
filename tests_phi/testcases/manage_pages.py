from tests_phi.testcases.test_base import TestBase
from tests_phi.utils import common_functions
from tests_phi.pages.login_page import LoginPage
from tests_phi.pages.dashboard_page import DashboardPage
from tests_phi.utils import constants
from tests_phi.utils import browser_helper
import logging
import pytest

class Test_ManagePage(TestBase):
    
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    path_page_name_1 = None
    path_page_name_2 = None
   
    @pytest.mark.usefixtures("clean_up_tc021")
    def test_da_mp_tc021(self):
        ''' Verify that user is able to edit the name of the page (Parent/Sibbling) successfully'''
          
        logging.info("set variables")
        page_name_1 = common_functions.random_string()
        page_name_2 = common_functions.random_string()
        page_name_3 = common_functions.random_string()
        page_name_4 = common_functions.random_string()
          
        logging.info("1. Login to Dashboard and login")
        self.login_page.go_to()
        self.login_page.login(constants.USERNAME, constants.VALID_PASSWORD)
          
        logging.info("2. Add page 1")
        self.dashboard_page.add_page(page_name_1)
          
        logging.info("3. Add page 2")
        self.dashboard_page.add_page(page_name_2, page_name_1)
          
        logging.info("4. Open Page 1")
        self.dashboard_page.open_page("Overview", page_name_1)
         
        logging.info("VP: %s page displays" % page_name_1)
        browser_helper.get_page_title()
        assert page_name_1 in browser_helper.get_page_title()
          
        logging.info("5. Edit Page 1 to other name")
        self.dashboard_page.edit_page(page_name_3)
          
        logging.info("VP: User is able to edit the name of parent page successfully")
        assert page_name_3 in browser_helper.get_page_title()
          
        logging.info("6. Open Page 2")
        self.dashboard_page.open_page("Overview", page_name_3, page_name_2)
         
        logging.info("VP: %s page displays" % page_name_2)
        assert page_name_2 in browser_helper.get_page_title()
          
        logging.info("7. Edit Page 2 to other name")
        self.dashboard_page.edit_page(page_name_4, page_name_3)
          
        logging.info("VP: User is able to edit the name of parent page successfully")
        assert page_name_4 in browser_helper.get_page_title()
         
        self.path_page_name_2 = "Overview", page_name_3, page_name_4
        self.path_page_name_1 = "Overview", page_name_3
        
    @pytest.mark.usefixtures("clean_up_tc022")
    def test_da_mp_tc022(self):
        '''Verify that user is unable to duplicate the name of sibbling page under the same parent page'''
          
        logging.info("set variables")
        page_name_1 = common_functions.random_string()
          
        logging.info("1. Login to Dashboard and login")
        self.login_page.go_to()
        self.login_page.login(constants.USERNAME,constants.VALID_PASSWORD)
          
        logging.info("2. Add page 1")
        self.dashboard_page.add_page(page_name_1)
          
        logging.info("3. Add other page with the same name with page 1")
        self.dashboard_page.select_global_selecting_item("Add Page")
        self.dashboard_page.enter_page_info(page_name_1)
        self.dashboard_page.submit_modal()
          
        logging.info("VP: '%s' message displays"% constants.EXISTING_PAGE_NAME_MESSAGE)
        assert browser_helper.get_alert_text() == constants.EXISTING_PAGE_NAME_MESSAGE.format(page_name_1)
         
        self.path_page_name_1 = "Overview", page_name_1
         
    @pytest.fixture()
    def clean_up_tc021(self):
        yield
        logging.info("Teardown: Delete page")
        self.dashboard_page.delete_page(self.path_page_name_2)
        self.dashboard_page.delete_page(self.path_page_name_1)
        self.dashboard_page.logout()
          
    @pytest.fixture()
    def clean_up_tc022(self):
        yield
        logging.info("Teardown: Dismiss Alert and modal")
        browser_helper.dismiss_alert()
        self.dashboard_page.dismiss_modal()
        logging.info("Teardown: Delete page")
        self.dashboard_page.delete_page(self.path_page_name_1)
        self.dashboard_page.logout()
