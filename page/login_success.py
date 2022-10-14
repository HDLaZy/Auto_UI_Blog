from page.base_page import BasePage


class LoginSuccessPage(BasePage):

    #用户名
    username=('i','username')
    #输入用户名
    def input_username(self,username):
        self.locate_element(*self.username).send_keys(username)

    #密码
    password=('i','password')
    #输入密码
    def input_password(self,password):
        self.locate_element(*self.password).send_keys(password)

    #提交
    submit=('i','submit')
    #点击登录
    def click_submit(self):
        self.locate_element(*self.submit).click()

    #主页
    index=('l','主页')
    #获取名称
    def get_index_name(self):
        return self.locate_element(*self.index).text

    #写博客
    write_blog=('l','写博客')
    #获取名称
    def get_write_name(self):
        return self.locate_element(*self.write_blog).text

    #注销
    logout_name=('l','注销')
    #获取名称
    def get_logout(self):
        return self.locate_element(*self.logout_name).text

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

    # 昵称
    list_nickname = ('id', 'nickname')
    # 获取昵称
    def get_nickname(self):
        nickname = self.locate_element(*self.list_nickname).text
        return nickname

    #左上角名字
    title_name = ("x", "/html/body/div[1]/div[1]/span")
    # 获取左上角名字
    def get_title_name(self):
        title_name = self.locate_element(*self.title_name).text
        return title_name

    #查看全文
    blog_text=("l",'查看全文 >>')
    def click_blog_text(self):
        blogs=self.locate_elements(*self.blog_text)
        if len(blogs)>0:
            blogs[0].click()