from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.basePage import BasePage
from page.mobileLogin import MobileLogin


class Setting(BasePage):
    _logout = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("退出").instance(0));')
    _sure = (By.ID, "com.xueqiu.android:id/md_buttonDefaultPositive")

    def logout(self):
        self.find(self._logout).click()
        self.find(self._sure).click()
        return MobileLogin()
