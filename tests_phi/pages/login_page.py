from selenpy.element.text_box import TextBox
from selenpy.support.conditions import be
from selenpy.support import browser
from selenpy.element.base_element import BaseElement
from tests_phi.utils import common_functions

class LoginPage():
    
    def __init__(self):
        self._lbl_login_title = BaseElement("//div[@class='ltext' and text()='Login']")
        self._txt_user_name = TextBox("id=username")
        self._txt_password = TextBox("id=password")
        self._btn_login = BaseElement("class=btn-login")
    
    def go_to(self):
        browser.open_url(common_functions.get_url())
        self._lbl_login_title.wait_until(be.visible)
     
    def login(self, user_name, password, successed = True):
        self._txt_user_name.wait_for_visible()
        self._txt_user_name.send_keys(user_name)
        self._txt_password.send_keys(password)
        self._btn_login.wait_until(be.visible)
        self._btn_login.click()
        if successed:
            self._btn_login.wait_for_invisible()
