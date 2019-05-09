from tests_trung.controls.button import Button
from tests_trung.pages.general_page import GeneralPage
from tests_trung.pages.general_settings_page import GeneralSettingPage


class DataProfilesPage(GeneralPage):

    general_settings_page = GeneralSettingPage()

    def __init__(self):
        self._btn_add_new = Button("//a[text()='Add New']")
        self._btn_delete = Button("//a[text()='Delete']")

    def open_add_new_profile(self):
        self._btn_add_new.wait_for_visible()
        self._btn_add_new.click()
        self.wait_for_page_loaded()

    def add_new_profile(self, name, item_type = None, related_data = None):
        self.open_add_new_profile()
        self.general_settings_page.add_new_profile(name, item_type, related_data)
