from appium import webdriver

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["ensureWebviewsHavePages"] = True
            caps["skipServerInstallation"] = True
            # 提升运行速度
            caps["skipDeviceInitialization"] = True
            caps["noReset"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()
            self.set_implicitly(3)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)