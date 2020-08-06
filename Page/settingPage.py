from Base.base import Base
from Page.pageElements import PageElements

"""登录后的设置界面"""


class SettingPage(Base):
    def __init__(self):
        Base.__init__(self)

    def scroll_setting(self):
        # 向上滑动
        self.scroll_ele()

    def click_logout(self):
        # 点击退出按钮并确认
        self.click_ele(PageElements.setting_logout_xpath)
        self.click_ele(PageElements.logout_confirm_xpath)
