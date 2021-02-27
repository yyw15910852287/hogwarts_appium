import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *

class TestGetAttr():
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
        # self.driver.quit()
        pass

    def test_get_attr(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        # 元素是否可用
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        # 坐标
        print(search_ele.get_attribute("bounds"))
        assert 'search' in search_ele.get_attribute("resource-id")

    def test_assert(self):
        a = 10
        b = 20
        assert a < b
        assert 'h' in 'this'

    def test_hamrest(self):
        # assert_that(10,equal_to(10),'这是一个提示' )
        # assert_that(8,close_to(10,2))
        assert_that("contains some string",contains_string("string"))
