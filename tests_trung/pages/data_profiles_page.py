from tests_trung.controls.button import Button
from tests_trung.pages.general_page import GeneralPage
from tests_trung.utils import browser_helper
from tests_trung.controls.label import Label


class DataProfilesPage(GeneralPage):

    def __init__(self):
        self._btn_add_new = Button("//a[text()='Add New']")
        self._btn_delete = Button("//a[text()='Delete']")
        self._lbl_list_data_profile = Label("//table[@class='GridView']//tr/td[count(//table[@class='GridView']//th[.='Data Profile']/preceding-sibling::*)+1]")

    def open_add_new_profile(self):
        self._btn_add_new.wait_for_visible()
        self._btn_add_new.click()
        browser_helper.wait_for_page_loaded()

    def get_list_data_profiles(self):
        list_dp = []
        for e in self._lbl_list_data_profile.find_elements():
            list_dp.append(e.text)
        return list_dp
