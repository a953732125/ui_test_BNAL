from Base.base import Base
from Page.pageElements import PageElements

"""个人账号页面"""


class AccountPage(Base):
    def __init__(self):
        Base.__init__(self)

    def click_setting(self):
        # 个人页面点击设置按钮
        self.click_ele(PageElements.my_account_setting)

    def get_account_info(self):
        # 个人信息页面的所有结果列表
        res = self.search_eles(PageElements.my_account_texts_class, timeout=2)
        return [i.text for i in res]
