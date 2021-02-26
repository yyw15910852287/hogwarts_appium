from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage
from app.page.member_invite import MemberInvite


class AddressList(BasePage):

    def add_member(self):
        self.find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        print("添加成员")
        return MemberInvite(self._driver)