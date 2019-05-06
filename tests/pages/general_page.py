from selenpy.support import browser
from selenpy.support.conditions import have
from selenpy.element.base_element import BaseElement
import random
import string

class GeneralPage():
    
    def __init__(self):
        pass
        
        
    def is_title_contains(self, title):
        return have.contains_title(title)
    
    
    def get_alert_text(self):
        return browser.switch_to_alert().text
    
    
    def dismiss_alert(self):
        browser.switch_to_alert().dismiss()


    def select_menu(self,dynamic_menu):
        items = dynamic_menu.split("/")
        for item in items:
            str_item = "//a[text()='%']"
            str_item = str_item.replace("%",item)
            element = BaseElement(str_item)
            element.wait_for_visible()
            element.click()

    def random_string(self, stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.sample(letters,stringLength))