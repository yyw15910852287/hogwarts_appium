from appium.webdriver.common.mobileby import MobileBy

from app.page.addresslist_page import AddressList
from app.page.base_page import BasePage


class Main(BasePage):

    def goto_message(self):
        pass

    def goto_addresslist(self):
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressList(self._driver)

    def goto_workbench(self):
        pass

    def goto_profile(self):
        pass
