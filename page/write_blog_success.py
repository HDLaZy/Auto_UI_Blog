from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from page.login_success import LoginSuccessPage


class WriteSuccessPage(LoginSuccessPage):
    #写博客
    def click_write_blog(self):
        self.locate_element(*self.write_blog).click()

    #标题
    title=('i','title')
    #写标题
    def input_title(self,title):
        self.locate_element(*self.title).send_keys(title)

    #发布
    button=('t',"button")
    #点击发布
    def click_up(self):
        self.locate_element(*self.button).click()

    #alert弹出框
    def click_alert(self):
        self.alert()

    #断言新添加文章
    blog_titles=('x','//*[@class="title"]')
    #获取最新的文章标题
    def get_title(self):
        titles=self.locate_elements(*self.blog_titles)
        return titles[-1].text

    #注销
    logout=('l','注销')
    def click_logout(self):
        self.locate_element(*self.logout).click()

if __name__=="__main__":
    driver=webdriver.Chrome()
    driver.get('http://81.68.218.227:8081')
    titles=driver.find_elements(By.XPATH,'//*[@class="title"]')
    print(titles[-1].text)


