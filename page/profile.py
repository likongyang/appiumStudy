
from selenium.webdriver.common.by import By
from page.basePage import BasePage
from page.chooseLoginWay import ChooseLoginWay


class Profile(BasePage):
    _loginButton = (By.ID, "com.xueqiu.android:id/tv_login")
    _setting = (By.ID, "com.xueqiu.android:id/action_setting")

    def toLogin(self):
        self.find(self._loginButton).click()
        return ChooseLoginWay()

    def toSetting(self):
        self.find(self._setting).click()
        return Setting()