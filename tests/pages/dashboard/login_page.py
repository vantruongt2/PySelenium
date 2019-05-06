from selenpy.element.text_box import TextBox
from selenpy.element.base_element import BaseElement
from tests.pages.dashboard.general_page import GeneralPage


class LoginPage(GeneralPage):
    
    _txt_username = TextBox("id=username")
    _txt_password = TextBox("id=password")
    _btn_login = BaseElement("class=btn-login")

    def __init__(self):
        pass

    def login(self, username, password):
        self._txt_username.send_keys(username)
        self._txt_password.send_keys(password)
        self._btn_login.click()
        
