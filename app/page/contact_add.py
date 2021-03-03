from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class ContactAdd(BasePage):

    def input_name(self):
        sleep(3)
        name_element = self.find(MobileBy.ID, "com.tencent.wework:id/b7m")
        name_element.send_keys("hogwarts_name1")
        return self

    def set_phonenum(self):
        sleep(3)
        tel_element = self.find(MobileBy.ID, "com.tencent.wework:id/fwi")
        tel_element.send_keys("15910852281")

        return self

    def click_save(self):
        from app.page.member_invite import MemberInvite
        sleep(3)
        self.find(MobileBy.ID, "com.tencent.wework:id/aj_").click()
        return MemberInvite(self._driver)