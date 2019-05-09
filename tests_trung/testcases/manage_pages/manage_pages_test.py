from tests_trung.testcases.test_base import TestBase
from tests_trung.pages.login_page import LoginPage
from tests_trung.utils import common, browser_helper
from tests_trung.utils import constants
import pytest
import logging
from tests_trung.data import aut_messages
from tests_trung.pages.dashboard_page import DashboardPage
from tests_trung.pages.general_page import GeneralPage


class Test_manage_page(TestBase):

    login_page = LoginPage()
    dashboard_page = DashboardPage()
    general_page = GeneralPage()

    _page_1 = common.random_string("Page1_")
    _page_2 = common.random_string("Page2_")
    _page_3 = common.random_string("Page3_")
    _page_4 = common.random_string("Page4_")
    _test_page = common.random_string("Test_")
    _test_child_page = common.random_string("TestChild_")

    @pytest.mark.usefixtures("clean_up_tc021")
    def test_da_mp_tc021(self):
        logging.info("1. Add new page 1")
        self.dashboard_page.add_new_page(self._page_1, constants.ROOT_PAGE)

        logging.info("Verify that Page 1 is added")
        assert self._page_1 in browser_helper.get_title()

        logging.info("2. Add new page 2")
        self.dashboard_page.add_new_page(self._page_2, self._page_1)

        logging.info("Verify that Page 2 is added")
        assert self._page_2 in browser_helper.get_title()

        logging.info("3. Select page 1")
        self.dashboard_page.select_page(self._page_1)

        logging.info("4. Edit name Page 1 to Page 3")
        self.dashboard_page.edit_page(self._page_3)

        logging.info("Verify that Page 3 is updated")
        assert self._page_3 in browser_helper.get_title()

        logging.info("5. Select Page 2")
        self.dashboard_page.select_page(self._page_3, self._page_2)

        logging.info("6. Edit name Page 2 to Page 4")
        self.dashboard_page.edit_page(self._page_4)

        logging.info("Verify that Page 4 is updated")
        assert self._page_4 in browser_helper.get_title()

    @pytest.mark.usefixtures("clean_up_tc022")
    def test_da_mp_tc022(self):
        logging.info("1. Add new page Test")
        self.dashboard_page.add_new_page(self._test_page, constants.ROOT_PAGE)

        logging.info("Verify that Test is added")
        assert self._test_page in browser_helper.get_title()

        logging.info("2. Add new page TestChild1 is child of Test page")
        self.dashboard_page.add_new_page(self._test_child_page, self._test_page)

        logging.info("Verify that TestChild1 is added")
        assert self._test_child_page in browser_helper.get_title()

        logging.info("3. Add new page TestChild1 is child of Test page")
        self.dashboard_page.add_new_page(
            self._test_child_page, self._test_page, False)

        logging.info(
            "Verify that warning message 'TestChild1 already exist. Please enter a diffrerent name.' appears")
        assert aut_messages.EXISTED_PAGE_WARN.format(self._test_child_page) in browser_helper.get_alert_text()

    @pytest.mark.usefixtures("clean_up_tc023")
    def test_da_mp_tc023(self):
        logging.info("1. Add new page 1")
        self.dashboard_page.add_new_page(self._page_1, constants.ROOT_PAGE)

        logging.info("Verify that Page 1 is added")
        assert self._page_1 in browser_helper.get_title()

        logging.info("2. Add new page 2")
        self.dashboard_page.add_new_page(self._page_2, self._page_1)

        logging.info("Verify that Page 2 is added")
        assert self._page_2 in browser_helper.get_title()

        logging.info("3. Go to the first created page")
        self.dashboard_page.select_page(self._page_1)

        logging.info("4. Edit another name into Page Name field")
        self.dashboard_page.edit_page(self._page_3)

        logging.info(
            "Verify that User is able to edit the parent page of the sibbling page successfully")
        assert self._page_3 in browser_helper.get_title()

    @pytest.mark.usefixtures("clean_up_tc024")
    def test_da_mp_tc024(self):
        logging.info("1. Add new page 1")
        self.dashboard_page.add_new_page(self._page_1, constants.ROOT_PAGE)

        logging.info("2. Add new page 2")
        self.dashboard_page.add_new_page(self._page_2, self._page_1)

        logging.info("3. Select page 1")
        self.dashboard_page.select_page(self._page_1)

        logging.info("Verify that Page 1 is added")
        assert self._page_1 in browser_helper.get_title()

        logging.info("4. Select Page 2")
        self.dashboard_page.select_page(self._page_1, self._page_2)

        logging.info("Verify that Page 2 is updated")
        assert self._page_2 in browser_helper.get_title()

    ''' CLEANING UP '''

    @pytest.fixture()
    def clean_up_tc021(self):
        logging.info("Navigate to Dashboard with valid user")
        self.login_page.go_to()
        self.login_page.login()
        yield
        logging.info("Delete the created pages")
        self.dashboard_page.delete_page(self._page_3, self._page_4)
        self.dashboard_page.delete_page(self._page_3)

    @pytest.fixture()
    def clean_up_tc022(self):
        yield
        logging.info("Dismiss alert and cancel modal")
        browser_helper.accept_alert()
        self.dashboard_page.cancel_modal()
        logging.info("Delete the created pages")
        self.dashboard_page.delete_page(self._test_page, self._test_child_page)
        self.dashboard_page.delete_page(self._test_page)

    @pytest.fixture()
    def clean_up_tc023(self):
        yield
        logging.info("Delete the created pages")
        self.dashboard_page.delete_page(self._page_3, self._page_2)
        self.dashboard_page.delete_page(self._page_3)

    @pytest.fixture()
    def clean_up_tc024(self):
        yield
        logging.info("Delete the created pages")
        self.dashboard_page.delete_page(self._page_1, self._page_2)
        self.dashboard_page.delete_page(self._page_1)
