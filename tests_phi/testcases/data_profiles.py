from tests_phi.testcases.test_base import TestBase
from tests_phi.pages.login_page import LoginPage
from tests_phi.pages.dashboard_page import DashboardPage
from tests_phi.utils import constants
from tests_phi.utils import browser_helper
from tests_phi.pages.data_profiles_page import DataProfilesPage
from tests_phi.pages.general_setting_pages import DAGeneralSettingsPage
import logging
import pytest

class Test_DataProfiles(TestBase):
    
    login_page = LoginPage()
    dashboard_page = DashboardPage()
    data_profiles_page = DataProfilesPage()
    da_general_setting_page = DAGeneralSettingsPage()
    
    data_test = [
        ("",constants.EMPTY_PROFILE_NAME_MESSAGE),
        (" /:*?<>|\"#[]{}=%;",constants.PROFILE_NAME_INCLUDE_INVALID_CHAR_MESSAGE),
        ("Test Case Execution", constants.PROFILE_NAME_EXIST_MESSAGE)]
    
    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self):
        logging.info("Pre 1. Log in Dashboard")
        self.login_page.go_to()
        self.login_page.login(constants.USERNAME, constants.VALID_PASSWORD)
          
        logging.info("Pre 2. Navigate to Data Profiles page")
        self.dashboard_page.click_administer_item("Data Profiles")
        
    @pytest.mark.usefixtures("clean_up")   
    @pytest.mark.parametrize("profile_name,err_message", data_test)
    def test_da_dp_tc069_tc070_tc071(self, profile_name, err_message):
        ''' - Verify that user is unable to proceed to next step or finish creating data profile if  "Name *" field is left empty
            - Verify that special characters ' /:*?<>|"#[]{}=%; 'is not allowed for input to "Name *" field
            - Verify that Data Profile names are not case sensitive
        '''     
        
        logging.info("1. Click on Add New")
        self.data_profiles_page.select_add_new_link()
          
        logging.info("2. Enter profile name = %s" % profile_name)
        self.da_general_setting_page.fill_general_setting_info(profile_name)
          
        logging.info("3. Click on Next Button")
        self.da_general_setting_page.click_next_button()
          
        logging.info("VP. Check dialog message '%s' appears", err_message)
        assert browser_helper.get_alert_text() == err_message
          
        logging.info("2. Click on Finish Button")
        browser_helper.dismiss_alert()
        self.da_general_setting_page.click_finish_button()
          
        logging.info("VP. Check dialog message '%s' appears" % err_message)
        assert browser_helper.get_alert_text() == err_message
        
    def test_da_dp_tc072_t073(self):
        ''' - Verify that all data profile types are listed under "Item Type" dropped down menu
            - Verify that all data profile types are listed in priority order under "Item Type" dropped down menu
        '''
        time_types_list = ["Test Modules", "Test Cases",
                            "Test Objectives", "Data Sets",
                             "Actions", "Interface Entities",
                             "Test Results", "Test Case Results",
                              "Test Suites","Bugs"]
        
        logging.info("1. Click on Add New")
        self.data_profiles_page.select_add_new_link()
         
        logging.info("VP. list of 'item types' displays as\
         'Test Modules>Test Cases> Test Objectives> Data Sets> Actions> Interface Entities>\
          Test Results> Test Cases results> Test Suites> Bugs")
        logging.info(self.da_general_setting_page.get_item_type_options())
        assert self.da_general_setting_page.get_item_type_options() == time_types_list
        
    @pytest.fixture()
    def clean_up(self):
        yield
        logging.info("Dismiss alert and go back to Data profiles")
        browser_helper.dismiss_alert()
        self.dashboard_page.click_administer_item("Data Profiles")
