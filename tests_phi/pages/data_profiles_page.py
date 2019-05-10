from selenpy.element.base_element import BaseElement

class DataProfilesPage():

    def __init__(self):
        self._lbl_dynamic_link = BaseElement("//a[text()='%s']")
        
    def select_add_new_link(self):
        self._lbl_dynamic_link.format("Add New")
        self._lbl_dynamic_link.wait_for_visible()
        self._lbl_dynamic_link.click()
