from selenium import webdriver
from selenium.webdriver.common.by import By

from page.base_page import BasePage

class ListBlogPage(BasePage):

    #博客链接
    blog=('l','博客')
    #点击博客页面
    def click_blog(self):
        self.locate_element(*self.blog).click()


    #页面句柄转换
    def change_handles(self):
        handles=self.get_handles()
        self.switch_handles(handles[-1])


    #昵称
    list_nickname=('id','nickname')
    #获取昵称
    def get_nickname(self):
        nickname=self.locate_element(*self.list_nickname).text
        return nickname

    #左上角名字
    title_name=("x","/html/body/div[1]/div[1]/span")
    #获取左上角名字
    def get_title_name(self):
        title_name=self.locate_element(*self.title_name).text
        return title_name

    #首页
    index_name=("l",'主页')
    #获取首页名字
    def get_index_name(self):
        index_name=self.locate_element(*self.index_name).text
        return index_name

    #github链接
    github_link=("i",'github')
    #点击链接,获取url地址
    def click_github(self):
        self.locate_element(*self.github_link).click()
        github_url=self.driver.current_url
        return github_url

    #csdn链接
    csdn_url=('i','csdn')
    #点击链接，获取url地址
    def click_csdn(self):
        self.locate_element(*self.csdn_url).click()
        csdc_url=self.driver.current_url
        return csdc_url


    #查看全文
    blog_text=("l",'查看全文 >>')
    def click_blog_text(self):
        blogs=self.locate_elements(*self.blog_text)
        if len(blogs)>0:
            blogs[0].click()


if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get("http://www.hdlazy.xyz/")
    driver.quit()