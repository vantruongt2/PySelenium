from selenpy.element.base_element import BaseElement
from selenpy.support import browser


class GeneralPage():
    
    _lbl_dashboard = BaseElement("id=header")
    _lbl_user_menu = BaseElement("//a[@href='#Welcome']")
    _lbl_logout = BaseElement("//a[contains(@href,'logout')]")
    _lbl_setting = BaseElement("class=mn-setting")
    
    
    def __init__(self):
        pass
    
    def log_out(self):
        if self._lbl_dashboard.is_element_displayed():
            self._lbl_user_menu.click()
            self._lbl_logout.click()
        else:
            pass

    def get_error_message(self):
        alert = browser.switch_to_alert()
        return alert.text
