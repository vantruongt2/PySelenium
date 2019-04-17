from selenpy.helper.exceptions import ConditionMismatchException
from abc import abstractmethod


class WebDriverCondition():

    @abstractmethod
    def fn(self, webdriver):
        pass

    def description(self):
        return self.__class__.__name__


class Title(WebDriverCondition):

    def __init__(self, exact_value):
        self.expected = exact_value

    def fn(self, webdriver):        
        actual = webdriver.title
        if not self.expected == actual:
            raise ConditionMismatchException(
                expected=self.expected,
                actual=actual)


title = Title
