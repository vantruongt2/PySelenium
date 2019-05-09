from selenpy.element.base_element import BaseElement
from selenpy.element.text_box import TextBox
from selenpy.element.combo_box import ComboBox
from selenpy.element.check_box import CheckBox
from selenpy.support import browser
from tests_phi.utils.constants import SHORT_TIME

class DashboardPage():

    def __init__(self):
        self._lbl_login_title = BaseElement("//div[@class='ltext' and text()='Login']")
        self._lbl_welcome_user = BaseElement("//a[@href='#Welcome']")
        self._lbl_logout = BaseElement("//a[@href='logout.do']")
        self._ico_global_setting = BaseElement("//li[@class='mn-setting']/a")
        self._txt_page_name = TextBox("id=name")
        self._cbb_parent_name = ComboBox("id=parent")
        self._cbb_num_of_column = ComboBox("id=columnnumber")
        self._cbb_display_after = ComboBox("id=afterpage")
        self._cb_public = CheckBox("id=ispublic")
        self._btn_dynamic_on_add_edit_new_page = BaseElement("//input[@class='button page_button' and @id='%s']")
        self._lbl_test_module_execution = BaseElement("//div[@title='Test Module Execution']")
        self._lbl_dynamic_global_setting_item = BaseElement("//li[@class='mn-setting']//a[text()='%s']")
        self._lbl_dynamic_label = BaseElement("//a[text()='%s']")

    def logout(self):
        self._lbl_welcome_user.wait_for_visible()
        self._lbl_welcome_user.click()
        self._lbl_logout.wait_for_visible()
        self._lbl_logout.click()
        self._lbl_welcome_user.wait_for_invisible()

    def add_page(self, page_name, parent_page = "Overview", success=True):
        self.select_global_selecting_item("Add Page")
        self.enter_page_info(page_name, parent_page)
        self.submit_modal()
        if success:
            self._txt_page_name.wait_for_invisible()
        
    def edit_page(self,page_name, parent_page = "Overview", success=True):
        self.select_global_selecting_item("Edit")
        self.enter_page_info(page_name, parent_page)
        self.submit_modal()
        if success:
            self._txt_page_name.wait_for_invisible()
        
    def submit_modal(self):
        self._btn_dynamic_on_add_edit_new_page.format("OK")
        self._btn_dynamic_on_add_edit_new_page.wait_for_visible()
        self._btn_dynamic_on_add_edit_new_page.click()
    
    def dismiss_modal(self):
        self._btn_dynamic_on_add_edit_new_page.format("Cancel")
        if self._btn_dynamic_on_add_edit_new_page.is_displayed(SHORT_TIME):
            self._btn_dynamic_on_add_edit_new_page.click()
        self._btn_dynamic_on_add_edit_new_page.wait_for_invisible()
        
    def enter_page_info(self,page_name, parent_page = "Overview"):
        self._txt_page_name.wait_for_visible()
        self._txt_page_name.find_element().clear()
        self._txt_page_name.send_keys(page_name)
        self._cbb_parent_name.wait_for_visible()
        self._cbb_parent_name.select_by_text_contains(parent_page)
           
    def select_global_selecting_item(self, item):
        self._ico_global_setting.wait_for_visible()
        self._ico_global_setting.click()
        self._lbl_dynamic_global_setting_item.format(item)
        self._lbl_dynamic_global_setting_item.wait_for_visible()
        self._lbl_dynamic_global_setting_item.click()
        
    def open_page(self,*page_name):
        for item in page_name:
            self._lbl_dynamic_label.format(item)
            self._lbl_dynamic_label.wait_for_visible()
            if item == page_name[-1]:
                self._lbl_dynamic_label.click()
            else:
                self._lbl_dynamic_label.move_to()
    
    def delete_page(self, page_name):
        self.open_page(*page_name)
        self.select_global_selecting_item("Delete")
        browser.get_alert().accept()
        self._lbl_test_module_execution.wait_for_visible()
