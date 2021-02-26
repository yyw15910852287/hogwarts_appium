# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeiXin():
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["ensureWebviewsHavePages"] = True
        caps["skipServerInstallation"] = True
        caps["skipDeviceInitialization"] = True
        caps["noReset"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        print("teardown")
        self.driver.quit()

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test_addcontact(self):
        print("添加联系人")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        name_element = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/b7m")
        name_element.send_keys("hogwarts_name1")
        tel_element = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fwi")
        tel_element.send_keys("15910852281")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/aj_").click()
        sleep(1)
        print(self.driver.page_source)
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))