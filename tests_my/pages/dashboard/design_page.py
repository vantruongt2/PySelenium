from tests_my.testcases.utils import constants, common
from selenpy.element.check_box import CheckBox
from selenpy.element.combo_box import ComboBox
from selenpy.element.text_box import TextBox
from selenpy.element.base_element import BaseElement
from tests_my.pages.dashboard.dashboard_page import DashboardPage


class DesignPage(DashboardPage):

    def __init__(self):
        super().__init__()
        self._txt_name_page = TextBox("css=#div_popup #name")
        self._cbb_parent_page = ComboBox("css=#parent")
        self._btn_ok = BaseElement("css=#OK")
        self._lbl_pop_up = BaseElement("css=#div_popup h2")
        self._cb_public = CheckBox("css=#div_popup #ispublic")
        self._cbb_number_column = ComboBox("css=#div_popup #columnnumber")
        self._cbb_display_after = ComboBox("css=#div_popup #afterpage")

    def _fill_page_info(self, namepage, parentpage=None, numbercolumns=None, displayafter=None, public=None):
        self._lbl_pop_up.wait_for_visible()
        self._txt_name_page.wait_for_visible()
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

    def _complete_page(self, namepage, parentpage=None, numbercolumns=None, displayafter=None, public=None):
        self._fill_page_info(namepage, parentpage, numbercolumns, displayafter, public)
        self._btn_ok.wait_for_visible()
        self._btn_ok.click()
        common.wait_for_page_loaded()

    def _add_page(self, namepage, parentpage=None, numbercolumns=None, displayafter=None, public=None):
        self.select_item_setting(constants.Settings.ADD_PAGE.value)
        self._complete_page(namepage, parentpage, numbercolumns, displayafter, public)

    def _edit_page(self, namepage, parentpage=None, numbercolumns=None, displayafter=None, public=None):
        self.select_item_setting(constants.Settings.EDIT.value)
        self._complete_page(namepage, parentpage, numbercolumns, displayafter, public)
