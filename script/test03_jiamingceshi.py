from time import sleep

import allure

import page
from page.page_jiamingceshi import PageJiamingceshi
from page.page_login import PageLogin
from tool.get_driver import GetDriver


@allure.feature("假名测试测试用例")
class TestJiamingceshi():
    @classmethod
    def setup_class(cls):
        cls.driver = GetDriver.get_app_driver()
        cls.login = PageLogin(cls.driver)
        cls.jiaming = PageJiamingceshi(cls.driver)
        cls.login.base_click_element(page.approve)
        try:
            cls.login.base_click_element(page.skip_user_desc)
        except:
            pass
        cls.login.pagelogin()
        cls.login.base_click_element(page.wsy_tab)

    @classmethod
    def teardown_class(cls):
        GetDriver.quit_app_driver()

    def test01_jiamingceshi(self):
        self.jiaming.pagejiamingceshi_click_start_study()
        self.jiaming.pagejiamingceshi_click_ceshi()
        while True:
            try:
                self.jiaming.pagejiamingceshi_get_ans()
            except:
                pass
            if self.jiaming.pagejiamingceshi_if_confirm_exist():
                self.jiaming.pagejiamingceshi_click_confirm()
            else:
                break

        try:
            print('正在进行断言')
            assert self.jiaming.base_find_element(page.study1_share_report)
        except Exception:
            raise