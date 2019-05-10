from tests_trung.controls.button import Button
from tests_trung.pages.general_page import GeneralPage
from selenpy.element.text_box import TextBox
from selenpy.element.combo_box import ComboBox


class GeneralSettingPage(GeneralPage):

    def __init__(self):
        self._btn_next = Button("css=input[value='Next']")
        self._btn_finish = Button("css=input[value='Finish']")
        self._btn_cancel = Button("css=input[value='Cancel']")
        self._txt_name = TextBox("id=txtProfileName")
        self._cbb_item_type = ComboBox("id=cbbEntityType")
        self._cbb_related_data = ComboBox("id=cbbSubReport")

    def next(self):
        self._btn_next.wait_for_visible()
        self._btn_next.click()

    def finish(self):
        self._btn_finish.wait_for_visible()
        self._btn_finish.click()

    def cancel(self):
        self._btn_cancel.wait_for_visible()
        self._btn_cancel.click()

    def enter_profile_information(self, name, item_type = None, related_data = None):
        self._txt_name.wait_for_visible()
        self._txt_name.clear()
        self._txt_name.send_keys(name)
        if item_type is not None and item_type is not "":
            self._cbb_item_type.select_by_text_contains(item_type)
        if related_data is not None and related_data is not "":
            self._cbb_related_data.select_by_text_contains(related_data)

    def get_item_type_options(self):
        return self._cbb_item_type.get_options()
