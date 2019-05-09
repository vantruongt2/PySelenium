from selenpy.helper.exceptions import ConditionMismatchException
from abc import abstractmethod
import re


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
        result = re.search(self.expected, actual)
        # if not self.expected == actual:
        if result == None:
            raise ConditionMismatchException(
                expected=self.expected,
                actual=actual)


title = Title


class ElementCondition():

    def description(self):
        return self.__class__.__name__

    @abstractmethod
    def fn(self, webelement):
        pass


class Visible(ElementCondition):

    def fn(self, element):
        if not element.is_displayed():
            raise ConditionMismatchException()
        return element


visible = Visible()


class Enabled(ElementCondition):

    def fn(self, element):
        if not element.is_enabled():
            raise ConditionMismatchException()
        return element


enabled = Enabled()


class Value(ElementCondition):

    def __init__(self, exact_value):
        self.expected = exact_value

    def fn(self, element):
        actual = element.get_attribute("value")
        if not self.expected == actual:
            raise ConditionMismatchException(
                expected=self.expected,
                actual=actual)
