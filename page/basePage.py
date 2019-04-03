from appium.webdriver import WebElement
from selenium.webdriver.common.by import By
from driver.appium import Appium

class BasePage():

    def __init__(self):
        pass

    def findBy(self,by=By.ID, value=None):
        return Appium.getDriver().find_element(by, value)

    def find(self, locator) -> WebElement:
        return self.findBy(*locator)
