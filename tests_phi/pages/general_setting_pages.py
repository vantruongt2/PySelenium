from selenpy.element.base_element import BaseElement
from selenpy.element.text_box import TextBox
from selenpy.element.combo_box import ComboBox

class DAGeneralSettingsPage():

    def __init__(self):
        self.dynamic_button = BaseElement("//input[@value='%s']")
        self._txt_name = TextBox("id=txtProfileName")
        self._cbb_type = ComboBox("id=cbbEntityType")
        self._cbb_related_data = ComboBox("id=cbbSubReport")
        
    def fill_general_setting_info(self, name, item_type = None, related_data = None):
        self._txt_name.wait_for_visible()
        self._txt_name.clear()
        self._txt_name.send_keys(name)
        if item_type is not None:
            self._cbb_type.select_by_visible_text(item_type)
        if related_data is not None:
            self._cbb_related_data.select_by_visible_text(related_data)
        
    def click_next_button(self):
        self.dynamic_button.format("Next")
        self.dynamic_button.wait_for_visible()
        self.dynamic_button.click()
    
    def click_finish_button(self):
        self.dynamic_button.format("Finish")
        self.dynamic_button.wait_for_visible()
        self.dynamic_button.click()

    def get_item_type_options(self):
        return self._cbb_type.get_options()
