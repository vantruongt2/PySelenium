from tests_trung.utils.menu_list import MenuList
from tests_trung.controls.menu import Menu


class GeneralPage():

    def __init__(self):
        self._mnu_welcome_user = Menu("css=[href='#Welcome']")

    def logout(self):
        self._mnu_welcome_user.select_menu(MenuList.LOGOUT.value)
        self._mnu_welcome_user.wait_for_invisible()
