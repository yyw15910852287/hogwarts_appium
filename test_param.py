import pytest
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver


class TestParam():

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['skipServerInstallation'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element(MobileBy.ID,'com.xueqiu.android:id/action_close').click()
        pass
        # self.driver.quit()

    @pytest.mark.parametrize('searchkey,type,expect_price',[
        ('alibaba','BABA',250),
        ('xiaomi','01810',28)
    ])
    def test_search(self,searchkey,type,expect_price):
        """
        1.打开雪球 应用
        2.点击 搜索框
        3.输入 搜索词 ‘alibab’ or 'xiaomi'...
        4.点击第一个搜索结果
        5.判断 股票价格
        :return:
        """
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/name").click()
        current_price = float(self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        # expect_price = 250
        assert_that(current_price,close_to(expect_price,expect_price*0.1))
