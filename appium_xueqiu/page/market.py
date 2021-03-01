from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # self.find(By.ID,"com.xueqiu.android:id/action_search").click()
        return Search(self._driver)