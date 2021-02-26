from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class MemberInvite(BasePage):

    def addmember_by_mamul(self):
        from app.page.contact_add import ContactAdd
        sleep(3)
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        print("手动输入添加")
        return ContactAdd(self._driver)

    def get_toast(self):
        sleep(3)
        toast = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast