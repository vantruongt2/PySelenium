from tests_my.testcases.utils import constants, common
from selenpy.element.base_element import BaseElement
from tests_my.testcases.utils.common import wait_for_page_loaded

class DashboardPage():

    def __init__(self):
        self._lbl_dashboard = BaseElement("id=header")
        self._lbl_user_menu = BaseElement("//a[@href='#Welcome']")
        self._lbl_logout = BaseElement("//a[contains(@href,'logout')]")
        self._lbl_setting = BaseElement("class=mn-setting")
        self._lbl_item_setting = BaseElement("//li[@class='mn-setting']//a[normalize-space()='%s']")
        self._lbl_menu_setting = BaseElement("//span[normalize-space()='Global Setting']")
        self._lbl_page = BaseElement("//a[normalize-space()='%s']")

    def is_At(self):
        return self._lbl_dashboard.is_displayed(constants.WAIT_CONDITION_TIME)

    def log_out(self):
        if self._lbl_dashboard.is_displayed():
            self._lbl_user_menu.click()
            self._lbl_logout.click()
        else:
            pass

    def get_message(self):
        common.get_alert_text

    def select_item_setting(self, item):
        self._lbl_setting.wait_for_visible()
        self._lbl_setting.click()
        self._lbl_item_setting.format(item)
        self._lbl_item_setting.click()

    def select_page(self, *pages):
        for page in pages:
            self._lbl_page.format(page)
            self._lbl_page.wait_for_visible()
            self._lbl_page.move_to()
            if page == pages[-1]:
                self._lbl_page.click()

    def delete_page(self, *pages):
        self.select_page(*pages)
        self.select_item_setting(constants.Settings.DELETE.value)
        common.accept_alert()
        wait_for_page_loaded()

    def get_title(self):
        return common.get_title()
