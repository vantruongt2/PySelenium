from selenpy.element.base_element import BaseElement


class Link(BaseElement):

    def __init__(self, locator):
        super().__init__(locator)
