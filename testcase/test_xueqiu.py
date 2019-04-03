import unittest

from driver.appium import Appium
from page.xueqiu import Xueqiu


class TestXueqiu(unittest.TestCase):

    def setUp(self):
        Appium.initDriver()
        print(Appium.driver)

    def test_search(self):
        pass