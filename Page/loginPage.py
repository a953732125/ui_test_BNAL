import time

from Base.base import Base
from Page.pageElements import PageElements

"""账号登录页面"""


class LoginPage(Base):
    def __init__(self):
        Base.__init__(self)

    def choose_login(self):
        # 选择已有账号
        self.click_ele(PageElements.choose_login_xpath)

    def send_info(self, num, pwd):
        # 输入账号密码
        self.send_ele(PageElements.login_account, num)
        self.send_ele(PageElements.login_password, pwd)

    def click_login(self):
        # 点击登录按钮
        self.click_ele(PageElements.login_btn)
        time.sleep(2)

    def wrong_msg(self):
        # 返回错误toast信息
        # 手机号错误
        try:
            wrong_msg = self.search_ele(PageElements.num_wrong_msg, timeout=0.5, poll=0.1)
            return wrong_msg.text
        # 密码错误
        except:
            wrong_msg = self.search_ele(PageElements.pwd_wrong_msg, timeout=0.5, poll=0.1)
            return wrong_msg.text

    def click_close(self):
        # 点击关闭按钮
        self.click_ele(PageElements.close_btn)
