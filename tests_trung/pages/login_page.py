from selenpy.element.text_box import TextBox
from tests_trung.controls.button import Button
from selenpy.support import browser
from tests_trung.utils.data_reader import DataReader
from tests_trung.utils import browser_helper


class LoginPage():

    data = DataReader()

    def __init__(self):
        self._txt_user_name = TextBox("id=username")
        self._txt_password = TextBox("id=password")
        self._btn_login = Button("css=.btn-login")

    def go_to(self):
        browser.open_url(self.data.get_url())
        self._txt_user_name.wait_for_visible()

    def login(self, user = data.get_username(), pwd = data.get_password()):
        self._txt_user_name.send_keys(user)
        self._txt_password.send_keys(pwd)
        self._btn_login.click()
        browser_helper.wait_for_ajax()
