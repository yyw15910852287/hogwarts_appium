from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.extensions.android.gsm import GsmCallActions
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
            # 不停止APP，不清除app数据，不卸载app
            'noReset':True,
            # 停止app，清除app数据卸载app
            # 'fullReset':True,
            # 不停止测试app的进程
            'dontStopAppOnReset':True,
            'deviceName':'127.0.0.1:7555',
            'autoGrantPermissions':True,
            # 自动启动模拟器 emulator -list-avds 中的 Pixel_23_6
            # 只能是安卓自带的模拟器 第三方的不可以
            # 'avd':'Pixel_23_6'
            'newCommandTimeout':300

        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        pass
        # self.driver.make_gsm_call('15910852286',GsmCallActions.CALL)
        # self.driver.send_sms('15910852286','hello appium api')
        # # 录屏 8.0版本以上可以 华为不可
        # self.driver.start_recording_screen()
        # # 开启飞行模式
        # self.driver.set_network_connection(1)
        # self.driver.get_screenshot_as_file('./photos/img.png')
        # sleep(3)
        # self.driver.set_network_connection(4)
        # sleep(3)
        # self.driver.stop_recording_screen()

