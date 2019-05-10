from tests_my.testcases.utils import constants, browser_helper
from selenpy.element.base_element import BaseElement
from selenpy.element.combo_box import ComboBox
from selenpy.element.check_box import CheckBox
from tests_my.pages.controls.text_box import TextBox


class DashboardPage():

    def __init__(self):
        self._dashboard = BaseElement("id=div_main_body")
        self._lbl_user_menu = BaseElement("//a[@href='#Welcome']")
        self._lbl_logout = BaseElement("//a[contains(@href,'logout')]")
        self._lbl_setting = BaseElement("class=mn-setting")
        self._lbl_item_setting = BaseElement("//li[@class='mn-setting']//a[normalize-space()='%s']")
        self._lbl_menu_setting = BaseElement("//span[normalize-space()='Global Setting']")
        self._lbl_page = BaseElement("//a[text()='%s']")
        self._txt_name_page = TextBox("css=#div_popup #name")
        self._cbb_parent_page = ComboBox("css=#parent")
        self._btn_ok = BaseElement("css=#OK")
        self._lbl_pop_up = BaseElement("css=#div_popup h2")
        self._cb_public = CheckBox("css=#div_popup #ispublic")
        self._cbb_number_column = ComboBox("css=#div_popup #columnnumber")
        self._cbb_display_after = ComboBox("css=#div_popup #afterpage")

    def is_at(self):
        return self._dashboard.is_displayed(constants.WAIT_CONDITION_TIME)

    def log_out(self):
        if self._dashboard.is_displayed():
            self._lbl_user_menu.click()
            self._lbl_logout.click()

    def select_item_setting(self, item):
        browser_helper.wait_for_page_loaded()
        self._lbl_setting.wait_for_visible()
        self._lbl_setting.click()
        self._lbl_item_setting.format(item)
        self._lbl_item_setting.click()

    def select_page(self, *pages):
        browser_helper.wait_for_page_loaded()
        for page in pages:
            self._lbl_page.format(page)
            self._lbl_page.wait_for_visible(constants.WAIT_CONDITION_TIME)
            self._lbl_page.move_to()
            if page == pages[-1]:
                self._lbl_page.click()

    def delete_page(self, *pages):
        self.select_page(*pages)
        self.select_item_setting(constants.Settings.DELETE.value)
        browser_helper.accept_alert()
        browser_helper.wait_for_page_loaded()

    def get_title(self):
        browser_helper.wait_for_page_loaded()
        return browser_helper.get_title()

    def fill_page_info(self, name_page, parent_page=None, number_columns=None, display_after=None, is_public=False):
        self._lbl_pop_up.wait_for_visible()
        self._txt_name_page.wait_for_visible()
        self._txt_name_page.send_keys(name_page)
        if parent_page is not None and parent_page is not "":
            self._cbb_parent_page.select_by_text_contains(parent_page)
        if number_columns is not None and number_columns is not "":
            self._cbb_number_column.wait_for_visible()
            self._cbb_number_column.select_by_visible_text(number_columns)
        if display_after is not None and display_after is not "":
            self._cbb_display_after.wait_for_visible()
            self._cbb_display_after.select_by_visible_text(display_after)
        if is_public == True:
            self._cb_public.wait_for_visible()
            self._cb_public.check()

    def submit_page(self, name_page, parent_page=None, number_columns=None, display_after=None, public=None):
        self.fill_page_info(name_page, parent_page, number_columns, display_after, public)
        self._btn_ok.wait_for_visible()
        self._btn_ok.click()

    def add_page(self, name_page, parent_page=None, number_columns=None, display_after=None, public=None):
        self.select_item_setting(constants.Settings.ADD_PAGE.value)
        self.submit_page(name_page, parent_page, number_columns, display_after, public)

    def edit_page(self, name_page, parent_page=None, number_columns=None, display_after=None, public=None):
        self.select_item_setting(constants.Settings.EDIT.value)
        self.submit_page(name_page, parent_page, number_columns, display_after, public)

