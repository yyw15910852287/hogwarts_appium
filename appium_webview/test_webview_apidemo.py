from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestBrowser():
    def setup(self):
        des_caps = {
            'platformName':'android',
            'platformVersion':'6.0',
            'appPackage':'com.touchboarder.android.api.demos',
            'appActivity':'com.example.android.apis.ApiDemos',
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
        self.driver.find_element_by_xpath("//*[@text='Views']").click()
        webview = "WebView"
        print(self.driver.contexts)
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{webview}").'
                                                        'instance(0));').click()
        print(self.driver.contexts)
        # self.driver.switch_to(self.driver.contexts[-1])
        # content-desc属性用ACCESSIBILITY_ID
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"i_am_a_textbox").send_keys("abc")
        # self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"i am a link").click()
        # print(self.driver.page_source)
