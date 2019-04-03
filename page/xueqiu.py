from selenium.webdriver.common.by import By

from page.basePage import BasePage
from page.profile import Profile
from page.search import Search


class Xueqiu(BasePage):
    _profile = (By.ID,"com.xueqiu.android:id/user_profile_container")
    _search = (By.ID, "home_search")

    def toProfile(self):
        self.find(self._profile).click()
        return Profile()

    def toSearch(self):
        self.find(self._search).click()
        return Search()

    def loaded(self):
        locations = ["x", "y"]
        while locations[-1] != locations[-2]:
            element = self.find(self._profile).location
            locations.append(element)
            print(locations)
