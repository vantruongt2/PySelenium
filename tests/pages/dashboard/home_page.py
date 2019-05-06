from tests.pages.dashboard.general_page import GeneralPage

class HomePage(GeneralPage):


    def __init__(self):
        pass
    
    def is_At(self):
        return self._lbl_dashboard.is_element_displayed()
        