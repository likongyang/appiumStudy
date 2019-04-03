from selenium.webdriver.common.by import By

from page.basePage import BasePage
from page.mobileLogin import MobileLogin


class ChooseLoginWay(BasePage):
    _mobileWay = (By.ID, "com.xueqiu.android:id/tv_login_by_phone_or_others")

    def toMobileLogin(self):
        self.find(self._mobileWay).click()
        return MobileLogin()