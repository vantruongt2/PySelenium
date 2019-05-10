from tests_my.testcases.test_base import TestBase
from tests_my.pages.dashboard.login_page import LoginPage
from tests_my.testcases.utils import common
from tests_my.pages.dashboard.dashboard_page import DashboardPage
import pytest
import logging


class Test_MainPage(TestBase):

    login_page = LoginPage()
    dashboard_page = DashboardPage()
    page1 = "page1" + common.random_string()
    page2 = "page2" + common.random_string()
    page3 = "page3" + common.random_string()
    page4 = "page4" + common.random_string()
    parent_page = "Overview"

    @pytest.fixture(scope="session")
    def setup_class(self):
        self.login_page.login()
        yield
        self.dashboard_page.delete_page(self.parent_page, self.page3, self.page4)
        self.dashboard_page.delete_page(self.parent_page, self.page3)
        self.dashboard_page.log_out()

    def test_main_page_tc_021(self, setup_class):

        logging.info("Add page1")
        self.dashboard_page.add_page(self.page1, self.parent_page)

        logging.info("Add page2")
        self.dashboard_page.add_page(self.page2, self.page1)

        logging.info("Select page1")
        self.dashboard_page.select_page(self.parent_page, self.page1)

        logging.info("Edit page1 to page3")
        self.dashboard_page.edit_page(self.page3)

        logging.info("Verify page3 is edited successfully")
        assert self.page3 in self.dashboard_page.get_title()

        logging.info("Select page2")
        self.dashboard_page.select_page(self.parent_page, self.page3, self.page2)

        logging.info("Edit page2 to page4")
        self.dashboard_page.edit_page(self.page4)

        logging.info("Verify page3 is edited successfully")
        assert self.page4 in self.dashboard_page.get_title()
