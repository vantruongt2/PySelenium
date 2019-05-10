from selenpy.element.text_box import TextBox
from selenpy.support.conditions import have
from selenpy.support import browser
from selenpy.element.base_element import BaseElement
from selenpy.element.combo_box import ComboBox
from tests_thien.utilities import constant, browser_helper
import os

class LoginPage():
  
    def __init__(self):
        self._cbb_repository = ComboBox("name=repository")
        self._txt_username = TextBox("id=username")
        self._txt_password = TextBox("id=password")
        self._btn_login = BaseElement("class=btn-login")
    
    def open(self):
        browser.open_url(os.getenv("url"))
        browser.wait_until(have.title(constant.DA_TITLE))
        
    def login(self, username=constant.DA_USER, password=constant.DA_PWD, success=True, repository=constant.DA_REPO):
        self._cbb_repository.select_by_visible_text(repository)
        self._txt_username.clear()
        self._txt_username.send_keys(username)
        self._txt_password.send_keys(password)
        self._btn_login.click()
        if success:
            self._btn_login.wait_for_invisible()
        
    def is_message_displayed(self, message):
        return browser_helper.get_alert_text() == message
