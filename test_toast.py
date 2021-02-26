from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestToast():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.touchboarder.android.api.demos'
        desired_caps['appActivity'] = 'com.example.android.apis.view.PopupMenu1'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
        # pass

    def test_toast(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='Make a Popup!']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='Search']").click()
        # print(self.driver.page_source)
        # 查找toast可以通过class（当前页面只有一个toast）
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        # 通过text包含查找
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup')]").text)

