from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName':'android',
            'platformVersion':'6.0',
            'appPackage':'com.xueqiu.android',
            'appActivity':'com.xueqiu.android.common.MainActivity',
            # 'browserName':'Browser',
            'noReset':True,
            'deviceName':'127.0.0.1:7555'
            # 'chromedriverExecutable':'*********'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webwiew(self):
        # 点击交易
        self.driver.find_element(MobileBy.XPATH,"//*[@text='交易']").click()
        A_locator = (MobileBy.XPATH,'//android.view.View[@content-desc="A股开户"]')
        print(self.driver.contexts)
        # 切换上下文到webview
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 点击‘A股开户’
        print(self.driver.window_handles)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()
        kaihu_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(kaihu_window)
        # 输入用户名和验证码，点击立即开户
        self.driver.find_element(MobileBy.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[2]/input').send_keys("12345678901")
