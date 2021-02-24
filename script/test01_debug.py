
import allure
from tool.get_driver import GetDriver
from tool.get_log import GetLogger

log = GetLogger.get_log()


@allure.feature("成功")
class TestDebug():

    @classmethod
    def setup_class(cls):
        cls.driver = GetDriver.get_app_driver()

    @classmethod
    def teardown_class(cls):
        GetDriver.quit_app_driver()

    def test01_debug(self):
        pass
