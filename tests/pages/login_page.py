from selenpy.element.text_box import TextBox
from selenpy.support.conditions import be
from selenpy.support import browser
from selenpy.element.base_element import BaseElement
from tests.utils import constants

class LoginPage():
    
    _lbl_login_title = BaseElement("//div[@class='ltext' and text()='Login']")
    _txt_user_name = TextBox("id=username")
    _txt_password = TextBox("id=password")
    _btn_login = BaseElement("class=btn-login")
    
    def __init__(self):
        pass
    
    def go_to_login_page(self):
        browser.open_url(constants.DASHBOARD_URL)
        self._lbl_login_title.wait_until(be.visible)
        
    def login(self, user_name, password):
        self._txt_user_name.wait_for_visible()
        self._txt_user_name.send_keys(user_name)
        self._txt_password.send_keys(password)
        self._btn_login.wait_until(be.visible)
        self._btn_login.click()
