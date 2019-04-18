from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


class FirefoxDriver():

    def create_driver(self, capabilities):
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(executable_path=GeckoDriverManager().install(),
                            options=options,
                            desired_capabilities=capabilities)
        
