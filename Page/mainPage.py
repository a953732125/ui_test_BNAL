from Base.base import Base
from Page.pageElements import PageElements

"""百年奥莱主界面"""


class MainPage(Base):
    def __init__(self):
        Base.__init__(self)

    # 关闭更新弹窗
    def choose_close(self):
        self.click_ele(PageElements.msg_close)

    # 点击导航栏 '我'
    def choose_me(self):
        self.click_ele(PageElements.me_btn_xpath)
