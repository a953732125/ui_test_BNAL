from selenium.webdriver.common.by import By

"""页面元素定位"""


class PageElements:
    """百年奥莱首页"""
    # 定位弹窗“x”
    msg_close = (By.ID, 'com.yunmall.lc:id/img_close')
    """百年奥莱下方按钮"""
    # “我”按钮
    me_btn_xpath = (By.XPATH, '//*[@text="我"]')
    """'我'页面"""
    # 选择已有账号
    choose_login_xpath = (By.XPATH, '//*[contains(@text,"已有账号")]')
    # 关闭按钮
    close_btn = (By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image')
    # 手机号注册按钮
    tel_register_xpath = (By.ID, 'com.yunmall.lc:id/register_button')
    """登录页面"""
    # 账号输入框
    login_account = (By.ID, 'com.yunmall.lc:id/logon_account_textview')
    # 密码输入框
    login_password = (By.ID, 'com.yunmall.lc:id/logon_password_textview')
    # 登录按钮
    login_btn = (By.ID, 'com.yunmall.lc:id/logon_button')
    # 账号不存在的弹窗
    num_wrong_msg = (By.XPATH, '//*[contains(@text,"此用户")]')
    # 密码错误的弹窗
    pwd_wrong_msg = (By.XPATH, '//*[@text="登录密码错误"]')
    """个人账户主界面"""
    # 用户界面的文字
    my_account_texts_class = (By.CLASS_NAME, 'android.widget.TextView')
    # 设置按钮
    my_account_setting = (By.ID, 'com.yunmall.lc:id/ymtitlebar_left_btn_image')
    """设置界面"""
    # 退出按钮
    setting_logout_xpath = (By.XPATH, '//*[@text="退出"]')
    # 确认退出弹窗
    logout_confirm_xpath = (By.XPATH, '//*[@text="确认"]')
