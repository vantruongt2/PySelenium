from tests_thien.testcases.test_base import TestBase
from tests_thien.pages.dashboard.login_page import LoginPage
from tests_thien.pages.dashboard.dashboard_page import DashboardPage
from tests_thien.utilities import utilities, constant
import pytest
import logging

class EditDeletePagesTest(TestBase):
    login_page = LoginPage()
    da_page = DashboardPage()
    _page1 = utilities.random_string("Page1")
    _page2 = utilities.random_string("Page2")
    _page3 = utilities.random_string("Page3")
    _page4 = utilities.random_string("Page4")
    
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

    @pytest.fixture()
    def clean_up_tc021(self):
        yield
        self.da_page.delete_page(constant.ROOT_PAGE,self._page3,self._page4)
        self.da_page.delete_page(constant.ROOT_PAGE,self._page3)
        self.da_page.log_out()
