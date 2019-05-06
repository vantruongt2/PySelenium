from selenpy.element.base_element import BaseElement
from selenpy.element.text_box import TextBox
from selenpy.element.combo_box import ComboBox
from selenpy.element.check_box import CheckBox
from tests.pages.general_page import GeneralPage
import logging

class DashboardPage(GeneralPage):
    
    _lbl_login_title = BaseElement("//div[@class='ltext' and text()='Login']")
    _lbl_welcome_user = BaseElement("//a[@href='#Welcome']")
    _lbl_logout = BaseElement("//a[@href='logout.do']")
    _ico_global_setting = BaseElement("class=mn-setting")
    _txt_page_name = TextBox("id=name")
    _cbb_parent_name = ComboBox("id=parent")
    _cbb_num_of_column = ComboBox("id=columnnumber")
    _cbb_display_after = ComboBox("id=afterpage")
    _cb_public = CheckBox("id=ispublic")

    def __init__(self):
        pass
    
    
    def logout(self):
        self._lbl_welcome_user.wait_for_visible()
        self._lbl_welcome_user.click()
        self._lbl_logout.wait_for_visible()
        self._lbl_logout.click()
        self._lbl_welcome_user.wait_for_invisible()


    def add_page(self, page_name, parent_page = "Overview", num_of_column = "3", display_after = "Execution Dashboard", public= False):
        self._ico_global_setting.wait_for_visible()
        self._ico_global_setting.click()
        self.select_menu("Add Page")
        self._txt_page_name.wait_for_visible()
        self._txt_page_name.send_keys(page_name)
        self._cbb_parent_name.wait_for_visible()
        self._cbb_parent_name.select_by_visible_text(parent_page)
        self._cbb_num_of_column.wait_for_visible()
        self._cbb_num_of_column.select_by_visible_text(num_of_column)
        self._cbb_display_after.wait_for_visible()
        self._cbb_display_after.select_by_visible_text(display_after)
        if public:
            self._cb_public.check()
        
        
        
        