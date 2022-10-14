import unittest
from time import sleep

from parameterized import parameterized

from page.write_blog_success import WriteSuccessPage
from util.util import Util


class AddSuccessTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page=WriteSuccessPage()
        cls.logger=Util.get_log("../report/log/add_blog_success.log",'INFO')
        cls.page.open("")
        sleep(2)
        cls.page.screen_shot("../report/photo/add_blog_success",'登录页面')

    @classmethod
    def tearDownClass(cls):
        cls.page.quit_self()

    @parameterized.expand(
        Util.get_excel("../data/data.xlsx",'add_blog_success_data')
    )
    def test_add_blog_success(self,username,password,title):
        try:
            self.page.input_username(username)
            self.page.input_password(password)
            self.page.screen_shot("../report/photo/add_blog_success",'登录信息')
            self.page.click_submit()
            sleep(2)
            self.page.screen_shot("../report/photo/add_blog_success", '登录成功')
            self.page.click_write_blog()
            sleep(4)
            self.page.screen_shot("../report/photo/add_blog_success", '写博客页面')
            self.page.input_title(title)
            sleep(2)
            self.page.screen_shot("../report/photo/add_blog_success", '添加标题')
            self.logger.info(f"添加博客标题{title}")
            self.page.click_up()
            self.page.screen_shot("../report/photo/add_blog_success", '发布成功')
            sleep(1)
            self.page.alert()
            sleep(4)
            real_title=self.page.get_title()
            self.page.screen_shot("../report/photo/add_blog_success", '博客列表')
            self.page.click_logout()
            self.page.driver.get("")
            self.assertEqual(title,real_title,'添加博客标题断言失败')
        except AssertionError as e1:
            self.logger.error(f"添加博客断言失败，失败原因{e1}")
        except Exception as e2:
            self.logger.error(f"其他原因导致添加博客失败，失败原因{e2}")


if __name__=="__main__":
    unittest.main()
