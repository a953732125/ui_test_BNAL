from appium import webdriver


class Driver:
    __driver_app = None

    @classmethod
    def get_app_driver(cls):
        if cls.__driver_app is None:
            desired_caps = {
                'platformName': 'Android',
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.yunmall.lc',
                'appActivity': 'com.yunmall.ymctoc.ui.activity.MainActivity',
                'automationName': 'uiautomator2'
            }
            cls.__driver_app = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            return cls.__driver_app
        else:
            return cls.__driver_app

    @classmethod
    def quit_app_driver(cls):
        if cls.__driver_app:
            cls.__driver_app.quit()
            cls.__driver_app = None