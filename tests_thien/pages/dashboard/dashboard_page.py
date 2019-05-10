from selenpy.element.base_element import BaseElement
from selenpy.element.text_box import TextBox
from selenpy.element.combo_box import ComboBox
from tests_thien.utilities import constant, browser_helper
from tests_thien.utilities.settings_list import SettingsList
from tests_thien.utilities.menu_list import MenuList

class DashboardPage():
    
    def __init__(self):
        self._btn_global_setting = BaseElement("class=mn-setting")
        self._txt_page_name = TextBox("id=name")
        self._cbb_parent_name = ComboBox("id=parent")
        self._btn_ok = BaseElement("id=OK")
        self._btn_cancel = BaseElement("id=Cancel")
        self._lbl_test_module_execution = BaseElement("//div[@title='Test Module Execution']")
        self._link_page_item= BaseElement("//div[@id='main-menu']//a[text()='%s']")
        self._item_menu = BaseElement("//a[text()='%s']")
    
    def page_title(self, title):
        return constant.DA_TITLE+ " - " +title
    
    def is_page_displayed(self, page_name):
        return browser_helper.get_title() == self.page_title(page_name)
    
    def select_menu_item(self, *menu_item):
        for item in menu_item:
            self._item_menu.format(item)
            self._item_menu.wait_for_visible()
            if item == menu_item[-1]:
                self._item_menu.click()
            else:
                self._item_menu.move_to()
        
    def log_out(self):
        self.select_menu_item(constant.DA_USER,MenuList.LOGOUT.value)
    
    def select_global_setting(self, name):
        self._btn_global_setting.wait_for_visible()
        self._btn_global_setting.move_to()
        self.select_menu_item(name)
        
    def fill_page_info(self, page_name, parent_name):
        self._txt_page_name.wait_for_visible()
        self._txt_page_name.clear()
        self._txt_page_name.send_keys(page_name)
        if parent_name is not None:
            self._cbb_parent_name.select_by_text_contains(parent_name)
    
    def dismiss_modal(self):
        self._btn_cancel.wait_for_visible()
        self._btn_cancel.click()
    
    def create_new_page(self, page_name, parent_name=constant.ROOT_PAGE, success=True):
        self.select_global_setting(SettingsList.ADD_PAGE.value)
        self.fill_page_info(page_name, parent_name)
        self._btn_ok.wait_for_visible()
        self._btn_ok.click()
        if success:
            self._txt_page_name.wait_for_invisible()
    
    def edit_page_info(self, page_name, parent_name=None, success=True):
        self.select_global_setting(SettingsList.EDIT.value)
        self.fill_page_info(page_name, parent_name)
        self._btn_ok.wait_for_visible()
        self._btn_ok.click()
        if success:
            self._txt_page_name.wait_for_invisible()
    
    def go_to_page(self, *page_name):
        self.select_menu_item(*page_name)
    
    def delete_page(self, *page_name):
        self.go_to_page(*page_name)
        self.select_global_setting(SettingsList.DELETE.value)
        browser_helper.accept_alert()
        self._lbl_test_module_execution.wait_for_visible()
