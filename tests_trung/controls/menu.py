from selenpy.element.base_element import BaseElement


class Menu(BaseElement):

    def __init__(self, locator):
        super().__init__(locator)
        self._mmu_item = BaseElement("//a[text()='%s']")

    def select_menu(self, *menu_path):
        self.move_to()
        for menu in menu_path:
            self._mmu_item.format(menu)
            if menu == menu_path[-1]:
                self._mmu_item.click()
            else:
                self._mmu_item.move_to()
