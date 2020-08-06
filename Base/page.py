from Page.mainPage import MainPage
from Page.loginPage import LoginPage
from Page.accountPage import AccountPage
from Page.settingPage import SettingPage

"""统一入口类"""


class Page:
    @classmethod
    def get_main(cls):
        # 返回主页面对象
        return MainPage()

    @classmethod
    def get_login(cls):
        # 返回登录页面对象
        return LoginPage()

    @classmethod
    def get_account(cls):
        # 返回个人对象
        return AccountPage()

    @classmethod
    def get_setting(cls):
        # 返回设置页面对象
        return SettingPage()
