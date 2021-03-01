from time import sleep

from selenium.webdriver.common.by import By

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.market import Market


class Main(BasePage):
    def goto_market(self):
        sleep(3)
        self.find(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        return Market(self._driver)