from tests_thien.testcases.test_base import TestBase
from tests_thien.pages.dashboard.login_page import LoginPage
from tests_thien.pages.dashboard.dashboard_page import DashboardPage
from tests_thien.utilities import utilities, constant, browser_helper
import pytest
import logging

class EditDeletePagesTest(TestBase):
    login_page = LoginPage()
    da_page = DashboardPage()
    _page1 = utilities.random_string("Page1")
    _page2 = utilities.random_string("Page2")
    _page3 = utilities.random_string("Page3")
    _page4 = utilities.random_string("Page4")
    _page_test = utilities.random_string("Test")
    _page_test_child = utilities.random_string("TestChild")
    
    @pytest.mark.usefixtures("clean_up_tc021")
    def test_021_edit_page_name_successful(self):
        logging.info("Verify that user can login specific repository successfully via Dashboard login page with correct credentials")
        self.login_page.open()
        self.login_page.login()
        self.da_page.create_new_page(self._page1)
        self.da_page.create_new_page(self._page2, self._page1)
        self.da_page.go_to_page(constant.ROOT_PAGE,self._page1)
        self.da_page.edit_page_info(self._page3)
        assert self.da_page.is_page_displayed(self._page3)
        self.da_page.go_to_page(constant.ROOT_PAGE,self._page3,self._page2)
        self.da_page.edit_page_info(self._page4)
        assert self.da_page.is_page_displayed(self._page4)

    @pytest.mark.usefixtures("clean_up_tc022")
    def test_022_cannot_create_page_duplicate_name(self):
        logging.info("Verify that user is unable to duplicate the name of sibbling page under the same parent page")
        self.da_page.create_new_page(self._page_test, None)
        self.da_page.create_new_page(self._page_test_child, self._page_test)
        self.da_page.create_new_page(self._page_test_child, self._page_test, False)
        assert browser_helper.get_alert_text() == constant.MSG_DUP_PAGE_NAME.format(self._page_test_child)

    @pytest.mark.usefixtures("clean_up_tc023")
    def test_023_edit_sibbling_page_successful(self):
        logging.info("Verify that user is able to edit the parent page of the sibbling page successfully")
        self.da_page.create_new_page(self._page1)
        self.da_page.create_new_page(self._page2,self._page1)
        self.da_page.go_to_page(constant.ROOT_PAGE,self._page1)
        self.da_page.edit_page_info(self._page3)
        assert self.da_page.is_page_displayed(self._page3)

    @pytest.mark.usefixtures("clean_up_tc024")
    def test_024_breadcrums_navigate_successful(self):
        logging.info("Verify that Bread Crums navigation is correct")
        self.da_page.create_new_page(self._page1)
        self.da_page.create_new_page(self._page2,self._page1)
        self.da_page.go_to_page(constant.ROOT_PAGE,self._page1)
        assert self.da_page.is_page_displayed(self._page1)
        self.da_page.go_to_page(constant.ROOT_PAGE,self._page1,self._page2)
        assert self.da_page.is_page_displayed(self._page2)

    @pytest.fixture()
    def clean_up_tc021(self):
        yield
        self.da_page.delete_page(constant.ROOT_PAGE,self._page3,self._page4)
        self.da_page.delete_page(constant.ROOT_PAGE,self._page3)
        
    @pytest.fixture()
    def clean_up_tc022(self):
        yield
        browser_helper.dismiss_alert()
        self.da_page.dismiss_modal()
        self.da_page.delete_page(self._page_test,self._page_test_child)
        self.da_page.delete_page(self._page_test)
        
    @pytest.fixture()
    def clean_up_tc023(self):
        yield
        self.da_page.delete_page(constant.ROOT_PAGE,self._page3,self._page2)
        self.da_page.delete_page(constant.ROOT_PAGE,self._page3)
        
    @pytest.fixture()
    def clean_up_tc024(self):
        yield
        self.da_page.delete_page(constant.ROOT_PAGE,self._page1,self._page2)
        self.da_page.delete_page(constant.ROOT_PAGE,self._page1)
        self.da_page.log_out()
