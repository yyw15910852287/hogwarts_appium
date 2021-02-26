from appium import webdriver

from app.page.base_page import BasePage
from app.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["ensureWebviewsHavePages"] = True
            caps["skipServerInstallation"] = True
            # 提升运行速度
            caps["skipDeviceInitialization"] = True
            caps["noReset"] = True
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.launch_app()
            self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)