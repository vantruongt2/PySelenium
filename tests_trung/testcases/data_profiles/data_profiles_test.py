from tests_trung.testcases.test_base import TestBase
from tests_trung.pages.login_page import LoginPage
import pytest
import logging
from tests_trung.pages.dashboard_page import DashboardPage
from tests_trung.pages.general_page import GeneralPage
from tests_trung.utils.menu_list import MenuList
from tests_trung.pages.data_profiles_page import DataProfilesPage
from tests_trung.pages.general_settings_page import GeneralSettingPage
from tests_trung.utils import browser_helper, constants
from tests_trung.data import aut_messages


class Test_data_profiles(TestBase):

    login_page = LoginPage()
    dashboard_page = DashboardPage()
    general_page = GeneralPage()
    data_profiles_page = DataProfilesPage()
    general_settings_page = GeneralSettingPage()

    testdata = [
        ("", aut_messages.MISSING_PROFILE_NAME_WARN),
        (constants.SPECIAL_STRING, aut_messages.INVALID_PROFILE_NAME_WARN),
        ("Functional Tests", aut_messages.DUPLICATE_PROFILE_WARN),
    ]

    @pytest.fixture(scope = "class", autouse = True)
    def pre_condition(self):
        logging.info("Navigate to Dashboard and login with valid user")
        self.login_page.go_to()
        self.login_page.login()

        logging.info("Navigate to Data Profiles page")
        self.dashboard_page.select_administer_option(MenuList.DATA_PROFILES.value)

    def test_da_dp_tc065(self):
        preset_data_profiles = ["Action Implementation By Status", "Functional Tests", "Test Case Execution", "Test Case Execution Failure Trend", "Test Case Execution History", "Test Case Execution Results", "Test Case Execution Trend", "Test Module Execution", "Test Module Execution Failure Trend", "Test Module Execution Failure Trend by Build", "Test Module Execution History", "Test Module Execution Results", "Test Module Execution Results Report", "Test Module Execution Trend", "Test Module Execution Trend by Build", "Test Module Implementation By Priority", "Test Module Implementation By Status", "Test Module Status per Assigned Users", "Test Objective Execution"]

        logging.info("Verify that Pre-set Data Profile are populated correctly in profiles page")
        assert preset_data_profiles == self.data_profiles_page.get_list_data_profiles()

    def test_da_dp_tc072(self):
        item_type_options = ["Test Modules", "Test Cases", "Test Objectives", "Data Sets", "Actions", "Interface Entities", "Test Results", "Test Case Results", "Test Suites", "Bugs"]

        logging.info("1. Open add new profile")
        self.data_profiles_page.open_add_new_profile()

        logging.info("Verify that all data profile types are listed under 'Item Type' are correctly")
        assert item_type_options == self.general_settings_page.get_item_type_options()

    @pytest.mark.usefixtures("clean_up_invalid_cases")
    @pytest.mark.parametrize("name_profile,alert_message", testdata)
    def test_invalid_profile_name(self, name_profile, alert_message):
        logging.info("1. Enter invalid data")
        self.general_settings_page.fill_profile_information(name_profile)

        logging.info("2. Click on 'Next Button'")
        self.general_settings_page.next()

        logging.info("Verify that dialog message '" + alert_message + "' appears")
        assert alert_message in browser_helper.get_alert_text()

        logging.info("3. Click on 'Finish Button'")
        browser_helper.dismiss_alert()
        self.general_settings_page.finish()

        logging.info("Verify that dialog message '" + alert_message + "' appears")
        assert alert_message in browser_helper.get_alert_text()

    ' PRE-CONDITION & CLEANING UP '

    @pytest.fixture()
    def clean_up_invalid_cases(self):
        yield
        logging.info("Cancel adding new profile")
        browser_helper.dismiss_alert()

