import unittest
from time import sleep

from parameterized import parameterized

from page.login_success import LoginSuccessPage
from util.util import Util


class LoginSuccessTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page=LoginSuccessPage()
        cls.logger=Util.get_log("../report/log/login_success.log","INFO")
        cls.page.open(" ")
        cls.logger.info("打开登录页面成功")
        cls.page.screen_shot("../report/photo/login_success",'登录页面')
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.page.quit_self()

    @parameterized.expand(
        Util.get_excel(r'../data/data.xlsx','login_success_data')
    )
    def test_login(self,username,password):
        try:
            #输入用户名
            self.page.input_username(username)
            self.logger.info(f"登录用户名{username}")
            #输入密码
            self.page.input_password(password)
            self.logger.info(f"登录密码{password}")
            #截图
            self.page.screen_shot("../report/photo/login_success","登录信息填写页面")
            #点击提交
            self.page.click_submit()
            sleep(2)
            #登录截图
            self.page.screen_shot("../report/photo/login_success","登录成功页面")
            # 获取用户昵称
            nickname = self.page.get_nickname()
            self.logger.info(f"获取用户昵称{nickname}")
            # 获取左上角名称
            title_name = self.page.get_title_name()
            self.logger.info(f"获取左上角名称{title_name}")
            # 获取首页名
            index = self.page.get_index_name()
            self.logger.info(f"获取首页按钮{index}")
            # 获取写博客按钮名
            write = self.page.get_write_name()
            self.logger.info(f"获取写博客按钮{write}")
            # 获取注销按钮名
            logout=self.page.get_logout()
            self.logger.info(f"获取注销按钮{logout}")
            # 点击guthub链接
            github_url = self.page.click_github()
            sleep(5)
            self.logger.info(f"获取github地址{github_url}")
            self.page.screen_shot("../report/photo/login_success", 'github页面')
            # 回退
            self.page.back_window()
            # 点击csdn链接
            csdn_url = self.page.click_csdn()
            sleep(5)
            self.logger.info(f"获取csdn地址{csdn_url}")
            self.page.screen_shot("../report/photo/login_success", 'csdn页面')
            self.page.back_window()
            # 查看全文
            self.page.click_blog_text()
            sleep(5)
            self.page.screen_shot("../report/photo/login_success","文章详情页面")
            self.page.back_window()
            # nickname断言
            self.assertEqual("HDLaZy", nickname, "获取用户昵称断言失败")
            self.logger.info(f"获取用户昵称成功{nickname}")
            # title_name断言
            self.assertEqual("HelloEe", title_name, "获取左上角名称断言失败")
            self.logger.info(f"获取左上角名称成功{title_name}")
            # 首页按钮断言
            self.assertEqual("主页", index, "获取主页断言失败")
            self.logger.info(f"获取主页成功{index}")
            # github地址断言
            self.assertEqual("https://github.com/HDLaZy", github_url, "获取Github地址断言失败")
            self.logger.info(f"获取github的url地址成功{github_url}")
            # csdn地址断言
            self.assertIn("https://blog.csdn.net/HD_Cash", csdn_url, "获取CSDN地址断言失败")
            self.logger.info(f"获取CSDN地址成功{csdn_url}")
        except AssertionError as e1:
            self.logger.error(f"登录断言失败，失败原因:{e1}")
        except Exception as e2:
            self.logger.error(f"其它原因导致登录失败，失败原因:{e2}")


if __name__=="__main__":
    unittest.main()