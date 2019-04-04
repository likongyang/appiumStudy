import pytest
from selenium.webdriver.common.by import By

from page.basePage import BasePage
from page.mobileLogin import MobileLogin
import unittest
from driver.appium import Appium
from page.xueqiu import Xueqiu


class TestLogin(unittest.TestCase):
    _zixuan = (By.XPATH, "//*[@text='自选' and contains(@resource-id, 'tab_name')]")

    def setUp(self):
        Appium.initDriver()

    @pytest.mark.parametrize("mobile, password", [
        ("18201845315", "1991kill"),
        ("18201845315", ""),
        ("", "1991kill")
    ])
    def test_login(self,mobile, password):
        Xueqiu().loaded()
        Xueqiu()\
            .toProfile()\
            .toLogin()\
            .toMobileLogin()\
            .changeToPasswordLogin()\
            .login(mobile, password)
        assert Xueqiu.find(self._zixuan).text == "自选"

    def tearDown(self):
        Xueqiu.toProfile().toSetting().logout()
