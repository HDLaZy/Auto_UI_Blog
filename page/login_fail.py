from page.base_page import BasePage


class LoginFailPage(BasePage):
    # 用户名
    username = ('i', 'username')

    # 输入用户名
    def input_username(self, username):
        self.locate_element(*self.username).send_keys(username)

    # 密码
    password = ('i', 'password')

    # 输入密码
    def input_password(self, password):
        self.locate_element(*self.password).send_keys(password)

    # 提交
    submit = ('i', 'submit')

    # 点击登录
    def click_submit(self):
        self.locate_element(*self.submit).click()

    #错误信息回显
    error=('i','error')
    #获取错误信息
    def get_error(self):
        return self.locate_element(*self.error).text

    #清空内容
    def clean_login(self):
        self.clean_text(*self.username)
        self.clean_text(*self.password)



