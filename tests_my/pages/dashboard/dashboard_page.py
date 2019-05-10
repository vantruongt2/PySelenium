from tests_my.testcases.utils import constants, browser_helper
from selenpy.element.base_element import BaseElement
from selenpy.element.text_box import TextBox
from selenpy.element.combo_box import ComboBox
from selenpy.element.check_box import CheckBox


class DashboardPage():

    def __init__(self):
        self._dashboard = BaseElement("id=div_main_body")
        self._lbl_user_menu = BaseElement("//a[@href='#Welcome']")
        self._lbl_logout = BaseElement("//a[contains(@href,'logout')]")
        self._lbl_setting = BaseElement("class=mn-setting")
        self._lbl_item_setting = BaseElement("//li[@class='mn-setting']//a[normalize-space()='%s']")
        self._lbl_menu_setting = BaseElement("//span[normalize-space()='Global Setting']")
        self._lbl_page = BaseElement("//a[normalize-space()='%s']")
        self._txt_name_page = TextBox("css=#div_popup #name")
        self._cbb_parent_page = ComboBox("css=#parent")
        self._btn_ok = BaseElement("css=#OK")
        self._lbl_pop_up = BaseElement("css=#div_popup h2")
        self._cb_public = CheckBox("css=#div_popup #ispublic")
        self._cbb_number_column = ComboBox("css=#div_popup #columnnumber")
        self._cbb_display_after = ComboBox("css=#div_popup #afterpage")

    def is_At(self):
        return self._dashboard.is_displayed(constants.WAIT_CONDITION_TIME)

    def log_out(self):
        if self._dashboard.is_displayed():
            self._lbl_user_menu.click()
            self._lbl_logout.click()
        else:
            pass

    def get_message(self):
        browser_helper.get_alert_text()

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
        browser_helper.accept_alert()
        browser_helper.wait_for_page_loaded()

    def get_title(self):
        return browser_helper.get_title()

    def fill_page_info(self, namepage, parentpage=None, numbercolumns=None, displayafter=None, public=None):
        self._lbl_pop_up.wait_for_visible()
        self._txt_name_page.wait_for_visible()
        self._txt_name_page.find_element().clear()
        self._txt_name_page.send_keys(namepage)
        if parentpage is not None:
            self._cbb_parent_page.select_by_text_contains(parentpage)
        if numbercolumns is not None:
            self._cbb_number_column.wait_for_visible()
            self._cbb_number_column.select_by_visible_text(numbercolumns)
        if displayafter is not None:
            self._cbb_display_after.wait_for_visible()
            self._cbb_display_after.select_by_visible_text(displayafter)
        if public is not None:
            if public == "check":
                self._cb_public.wait_for_visible()
                self._cb_public.check()

    def submit_page(self, namepage, parentpage=None, numbercolumns=None, displayafter=None, public=None):
        self.fill_page_info(namepage, parentpage, numbercolumns, displayafter, public)
        self.accept_page_info()
        browser_helper.wait_for_page_loaded()

    def add_page(self, namepage, parentpage=None, numbercolumns=None, displayafter=None, public=None):
        self.select_item_setting(constants.Settings.ADD_PAGE.value)
        self.submit_page(namepage, parentpage, numbercolumns, displayafter, public)

    def edit_page(self, namepage, parentpage=None, numbercolumns=None, displayafter=None, public=None):
        self.select_item_setting(constants.Settings.EDIT.value)
        self.submit_page(namepage, parentpage, numbercolumns, displayafter, public)

    def accept_page_info(self):
        self._btn_ok.wait_for_visible()
        self._btn_ok.click()
