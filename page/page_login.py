import page
from base.base import Base


class PageLogin(Base):

    # 点击我的按钮
    def pagelogin_click_mine(self):
        self.base_click_element(page.wd_tab)

    # 调起一键登录
    def pagelogin_call_login(self):
        self.base_click_element(page.wd_login)

    # 点击登录按钮
    def pagelogin_click_otherstyle(self):
        self.base_click_element(page.login_otherstyle)

    def pagelogin_click_namepwd(self):
        self.base_click_element(page.login_namepwd)

    def pagelogin_input_username(self, username='11100009001'):
        self.base_input_value(page.login_username, username)

    def pagelogin_input_password(self, password='123456'):
        self.base_input_value(page.login_password, password)

    def pagelogin_click_submit(self):
        self.base_click_element(page.login_submit)

    # 业务组合方法
    def pagelogin(self):
        self.pagelogin_click_mine()
        self.pagelogin_call_login()
        self.pagelogin_click_otherstyle()
        self.pagelogin_click_namepwd()
        self.pagelogin_input_username()
        self.pagelogin_input_password()
        self.pagelogin_click_submit()
