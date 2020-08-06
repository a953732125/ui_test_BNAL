from Base.page import Page
from Base.driver import Driver
from Base.getData import GetData
import time
import pytest


def get_data():
    right_data = []
    data = GetData.get_json_data('login.json')
    for i in data['right_data']:
        right_data.append(
            (
                i['num'],
                i['pwd'],
                i['desc']
            )
        )
    return right_data


class TestLogin:

    # 开头运行一次,关闭更新弹窗
    def setup_class(self):
        self.flag = True  # 设置flag,如果flag为False则关闭登录框
        Page.get_main().choose_close()

    def setup(self):
        Page.get_main().choose_me()  # 点击'我'按钮
        Page.get_login().choose_login()  # 选择已有账号登录

    @pytest.mark.parametrize('num,pwd,desc', get_data())
    def test_login_right(self, num, pwd, desc):
        Page.get_login().send_info(num, pwd)  # 输入账号密码
        Page.get_login().click_login()  # 点击登录按钮
        try:
            assert 'lq_0729164728_kkb' in Page.get_account().get_account_info()  # 断言账号是否登录
        except:
            self.flag = False
            print(Page.get_login().wrong_msg())  # 打印错误的toast提示弹窗
            assert desc in Page.get_login().wrong_msg()

    def teardown(self):
        if self.flag:
            Page.get_account().click_setting()  # 点击设置按钮
            time.sleep(2)
            Page.get_setting().scroll_setting()  # 设置界面往下滑动
            Page.get_setting().click_logout()  # 点击退出并确认
        else:
            Page.get_login().click_close()

    def teardown_class(self):
        time.sleep(2)
        Driver.quit_app_driver()  # 关闭驱动
