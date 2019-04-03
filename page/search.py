from selenium.webdriver.common.by import By

from page.basePage import BasePage


class Search(BasePage):
    _search = (By.ID, "search_input_text")



    def search(self, keyword):
        self.find(self._search).send_keys(keyword)
        return self

    # def getUserName(self):
    #     self.find(self._user).click()
    #     self.find(self._username).text
    #
    # def getStocks(self):
    #     return self.find(self._stockName).text
    #
    # def cancel(self):
    #     self.find(self._cancel).click()
    #
    # def followFirst(self):
    #     elements = self.findAll(self._follow)
    #     if len(elements) == 2:
    #         elements[0].click()
    #
    #     return self