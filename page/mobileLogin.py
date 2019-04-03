from selenium.webdriver.common.by import By

from page.basePage import BasePage
from page.xueqiu import Xueqiu


class MobileLogin(BasePage):
    _topw = (By.ID, "com.xueqiu.android:id/tv_login_with_account")
    _account = (By.ID, "com.xueqiu.android:id/login_account")
    _password = (By.ID, "com.xueqiu.android:id/login_password")
    _loginButton = (By.ID, "com.xueqiu.android:id/button_next")

    def changeToPasswordLogin(self):
        self.find(self._topw).click()
        return self

    def login(self, mobile, password):
        self.find(self._account).send_keys(mobile)
        self.find(self._password).send_keys(password)
        self.find(self._loginButton).click()
        return Xueqiu()
