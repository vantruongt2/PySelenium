from selenpy.element.base_element import BaseElement
from selenium.webdriver.support.ui import Select


class ComboBox(BaseElement):
    _s = None    

    def __init__(self, locator):
        super().__init__(locator)    

    @property
    def _select(self):
        # if self._s is None:
        self._s = Select(self.find_element())
        return self._s

    def is_checked(self):
        return self._select().is_selected()

    def select_by_value(self, value):        
        self._select.select_by_value(value)

    def select_by_index(self, idx):    
        self._select.select_by_index(idx)

    def select_by_visible_text(self, text):
        self._select.select_by_visible_text(text)

    def select_by_text_contains(self, text):
        for o in self._select.options:
            if text in o.text:
                o.click()
                break

    @property
    def first_selected_text(self):        
        return self._select.first_selected_option.text

    def get_options(self):
        ops = []
        for o in self._select.options:
            ops.append(o.text)
        return ops

    def select_dynamic_menu(self, dynamic_menu):
        self.move_to()
        items = dynamic_menu.split(">")
        for item in items:
            menu_item = BaseElement("//a[text()='%s']")
            menu_item.format(item)
            if item == items[-1]: 
                menu_item.click()
            else:
                menu_item.move_to()
