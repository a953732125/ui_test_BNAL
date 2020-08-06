from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import Driver


class Base:
    def __init__(self):
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll=1.0):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, time=5, poll=1.0):
        self.search_ele(loc, time, poll).click()

    def send_ele(self, loc, text, timeout=5, poll=0.5):
        input_text = self.search_ele(loc, timeout, poll)
        input_text.clear()
        input_text.send_keys(text)

    def scroll_ele(self, tag=1):
        size = self.driver.get_window_size()  # 获取屏幕大小
        width = size.get('width')  # 获取宽
        height = size.get('height')  # 获取高
        if tag == 1:  # 向上滑动
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)
        elif tag == 2:  # 向下滑动
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)
        elif tag == 3:  # 向左滑动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)
        elif tag == 4:  # 向右滑动
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)
