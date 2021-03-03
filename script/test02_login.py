import allure

import page
from page.page_login import PageLogin
from tool.get_driver import GetDriver
from tool.get_log import GetLogger

log = GetLogger.get_log()


@allure.feature("登录测试用例")
class TestLogin():

    @classmethod
    def setup_class(cls):
        cls.driver = GetDriver.get_app_driver()
        cls.login = PageLogin(cls.driver)
        cls.login.base_click_element(page.approve)
        try:
            cls.login.base_click_element(page.skip_user_desc)
        except:
            pass

    @classmethod
    def teardown_class(cls):
        GetDriver.quit_app_driver()

    def test01_login(self):
        self.login.pagelogin()
        try:
            assert self.login.base_find_element(page.wd_username)
            print('登录成功')
        except:
            print('登录失败')
            raise
