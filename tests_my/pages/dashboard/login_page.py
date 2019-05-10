from selenpy.element.base_element import BaseElement
from selenpy.element.combo_box import ComboBox
from tests_my.testcases.utils import constants
from tests_my.pages.controls.text_box import TextBox


class LoginPage():

    def __init__(self):
        self._txt_username = TextBox("id=username")
        self._txt_password = TextBox("id=password")
        self._btn_login = BaseElement("class=btn-login")
        self._cbb_repository = ComboBox("id=repository")

    def fill_info_login(self, username, password, repository):
        self._cbb_repository.wait_for_visible()
        if repository is None:
            self._cbb_repository.select_by_visible_text(constants.REPOSITORY_DEFAULT)
        else:
            self._cbb_repository.select_by_visible_text(repository)
        self._txt_username.send_keys(username)
        self._txt_password.send_keys(password)

    def login(self, username=constants.USER_NAME, password=constants.PASSWORD, repository=None):
        self.fill_info_login(username, password, repository)
        self.submit_login()

    def submit_login(self):
        self._btn_login.wait_for_visible()
        self._btn_login.click()
