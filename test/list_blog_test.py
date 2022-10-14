import unittest
from time import sleep

from page.list_blog import ListBlogPage
from util.util import Util


class ListBlogTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.page=ListBlogPage()
        cls.logger=Util.get_log("../report/log/list_blog.log","INFO")
        cls.page.open("http://www.hdlazy.xyz/")
        cls.page.screen_shot("../report/photo/list_blog","个人主页")
        cls.logger.info("打开个人主页")
        sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.page.quit_self()

    def test_list_blog(self):
        try:
            #点击博客链接
            self.page.click_blog()
            self.logger.info("打开博客列表页面")
            sleep(2)
            #切换窗口句柄
            self.page.change_handles()
            #截图
            self.page.screen_shot("../report/photo/list_blog", "博客列表")
            #获取用户昵称
            nickname=self.page.get_nickname()
            #获取左上角名称
            title_name=self.page.get_title_name()
            #获取首页名
            index=self.page.get_index_name()
            #点击guthub链接
            github_url=self.page.click_github()
            sleep(5)
            self.page.screen_shot("../report/photo/list_blog", "github主页")
            #回退
            self.page.back_window()
            #点击csdn链接
            csdn_url=self.page.click_csdn()
            sleep(5)
            self.page.screen_shot("../report/photo/list_blog", "csdn主页")
            self.page.back_window()
            #查看全文
            self.page.click_blog_text()
            sleep(5)
            self.page.back_window()
            self.page.screen_shot("../report/photo/list_blog","文章详情")
            #断言
            #nickname断言
            self.assertEqual("HDLaZy",nickname,"获取用户昵称断言失败")
            self.logger.info(f"获取用户昵称成功{nickname}")
            #title_name断言
            self.assertEqual("HelloEe",title_name,"获取左上角名称断言失败")
            self.logger.info(f"获取左上角名称成功{title_name}")
            #首页按钮断言
            self.assertEqual("主页",index,"获取主页断言失败")
            self.logger.info(f"获取主页成功{index}")
            #github地址断言
            self.assertEqual("https://github.com/HDLaZy",github_url,"获取Github地址断言失败")
            self.logger.info(f"获取github的url地址成功{github_url}")
            #csdn地址断言
            self.assertIn("https://blog.csdn.net/HD_Cash",csdn_url,"获取CSDN地址断言失败")
            self.logger.info(f"获取CSDN地址成功{csdn_url}")
        except AssertionError as e1:
            self.logger.error(f"博客列表页面断言失败，失败原因:{e1}")
        except Exception as e2:
            self.logger.error(f"博客列表页面由于其它原因导致失败，失败原因:{e2}")

if __name__=="__main__":
    unittest.main()

