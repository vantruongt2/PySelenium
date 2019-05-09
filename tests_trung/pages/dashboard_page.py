from selenpy.element.text_box import TextBox
from tests_trung.controls.button import Button
from tests_trung.controls.label import Label
from selenpy.element.combo_box import ComboBox
from tests_trung.controls.check_box import CheckBox
from tests_trung.controls.menu import Menu
from tests_trung.utils.menu_list import MenuList
from tests_trung.pages.general_page import GeneralPage
from tests_trung.utils import browser_helper


class DashboardPage(GeneralPage):

    def __init__(self):
        super().__init__()
        self._mnu_administer = Menu("css=[href='#Administer']")
        self._mmu_global_setting = Menu("css=.mn-setting")
        self._mnu_overview = Menu("//div[@id='main-menu']//a[text()='Overview']")
        self._lbl_new_page_title = Label("css=#div_popup h2")
        self._txt_name = TextBox("css=#div_popup #name")
        self._cbb_parent = ComboBox("css=#div_popup #parent")
        self._cbb_number_of_column = ComboBox("css=#div_popup #columnnumber")
        self._cbb_display_after = ComboBox("css=#div_popup #afterpage")
        self._chk_is_public = CheckBox("css=#div_popup #ispublic")
        self._btn_ok = Button("css=#div_popup #OK")
        self._btn_cancel = Button("css=#div_popup #Cancel")

    def select_global_setting_option(self, option):
        self._mmu_global_setting.wait_for_visible()
        self._mmu_global_setting.select_menu(option)

    def select_page(self, *link):
        self._mnu_overview.wait_for_visible()
        self._mnu_overview.select_menu(*link)

    def delete_page(self, *page_link):
        self.select_page(*page_link)
        self.select_global_setting_option(MenuList.DELETE.value)
        browser_helper.accept_alert()
        self._mmu_global_setting.wait_for_visible()

    def add_new_page(self, name, parent = None, succeed = True):
        self.select_global_setting_option(MenuList.ADD_PAGE.value)
        self.enter_new_page_information(name, parent)
        self.submit_modal()
        if succeed:
            self._lbl_new_page_title.wait_for_invisible()

    def edit_page(self, name, parent = None, succeed = True):
        self.select_global_setting_option(MenuList.EDIT.value)
        self.enter_new_page_information(name, parent)
        self.submit_modal()
        if succeed:
            self._lbl_new_page_title.wait_for_invisible()

    def enter_new_page_information(self, name, parent):
        self._lbl_new_page_title.wait_for_visible()
        self._txt_name.clear()
        self._txt_name.send_keys(name)
        if parent is not None:
            self._cbb_parent.select_by_text_contains(parent)

    def submit_modal(self):
        self._btn_ok.wait_for_visible()
        self._btn_ok.click()

    def cancel_modal(self):
        self._btn_cancel.wait_for_visible()
        self._btn_cancel.click()

    def select_administer_option(self, option):
        self._mnu_administer.wait_for_visible()
        self._mnu_administer.select_menu(option)
