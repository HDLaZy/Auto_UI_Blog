import unittest
from time import sleep

from parameterized import parameterized

from page.login_fail import LoginFailPage
from util.util import Util


class LoginFailTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page=LoginFailPage()
        cls.logger=Util.get_log("../report/log/login_fail.log","INFO")
        cls.page.open("")
        cls.page.screen_shot("../report/photo/login_fail","登录页面")
        cls.logger.info("打开登录页面成功")


    @classmethod
    def tearDownClass(cls):
        cls.page.quit_self()

    @parameterized.expand(
        Util.get_excel("../data/data.xlsx","login_fail_data")
    )
    def test_login_fail(self,username,password):
        try:
            self.page.input_username(username)
            self.logger.info(f"登录失败用例，输入用户名{username}")
            self.page.input_password(password)
            self.logger.info(f"登录失败用例，输入面膜{password}")
            sleep(2)
            self.page.screen_shot("../report/photo/login_fail","输入登录信息截图")
            self.page.click_submit()
            sleep(2)
            error=self.page.get_error()
            self.logger.info(f"登录失败用例，错误信息{error}")
            self.page.screen_shot("../report/photo/login_fail",f"{error}截图")
            self.page.clean_login()
            self.assertIn(error,['账号不存在','账号或密码错误'],'登录失败回显信息断言失败')
        except AssertionError as e1:
            self.logger.error(f"登陆失败断言错误，错误原因:{e1}")
        except Exception as e2:
            self.logger.error(f"其它原因导致断言错误,错误原因:{e2}")

if __name__=="__main__":
    unittest.main()
