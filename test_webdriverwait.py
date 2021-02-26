from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver


class TestWebDriverWait():

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # 显示等待：用来处理隐式等待无法解决的一些问题（比如文件上传）
    def test_wait(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()

        locator = (MobileBy.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # WebDriverWait(self.driver,10).until(lambda x:x.find_element(*locator))
        ele = self.driver.find_element(*locator)
        current_price = float(ele.text)
        expected_price = 250
        print(f"当前09988对应的股价是：{current_price}")
        # assert current_price > 200
        assert_that(current_price,close_to(expected_price,expected_price*0.1))
