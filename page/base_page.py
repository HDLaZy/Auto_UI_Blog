"""
基础页面类,对webdriver的API进行二次封装
"""
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select


class BasePage():

    #初始化方法，创建浏览器对象
    def __init__(self, browser='chrome'):
        # 根据参数browser，创建相应的浏览器对象
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'safari':
            self.driver = webdriver.Safari()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        elif browser == 'opera':
            self.driver = webdriver.Opera()
        elif browser == 'edge':
            self.driver = webdriver.Edge()
        else:
            self.driver = webdriver.Chrome()

    #退出浏览器
    def quit_self(self):
        sleep(5)
        self.driver.quit()

    #关闭浏览器
    def close_self(self):
        sleep(5)
        self.driver.close()

    # 打开指定页面并最大化窗口，设置隐式等待时长
    def open(self, url, timeout=10):
        self.driver.get(url)

    # 将定位方式及其值封装为元组
    def get_locator(self, by, value):
        locator = ()
        if by == 'id' or by == 'i':
            locator = (By.ID, value)
        elif by == 'name' or by == 'n':
            locator = (By.NAME, value)
        elif by == 'class_name' or by == 'c':
            locator = (By.CLASS_NAME, value)
        elif by == 'tag_name' or by == 't':
            locator = (By.TAG_NAME, value)
        elif by == 'link_text' or by == 'l':
            locator = (By.LINK_TEXT, value)
        elif by == 'partial_link_text' or by == 'p':
            locator = (By.PARTIAL_LINK_TEXT, value)
        elif by == 'css_selector' or by == 'css':
            locator = (By.CSS_SELECTOR, value)
        elif by == 'xpath' or by == 'x':
            locator = (By.XPATH, value)
        else:
            locator = (By.ID, value)
        return locator

    # 定位单个元素（含等待逻辑）
    def locate_element(self, by, value, poll_frequency = 0.2, timeout = 5):
        locator = self.get_locator(by, value)
        # 最大询问次数
        n = timeout / poll_frequency
        while n > 0:
            try:
                # 拆包，如果定位到元素将其返回
                element = self.driver.find_element(locator[0], locator[1])
                return element
            except Exception:
                # 定位不到，在异常捕获中让程序睡眠0.2秒，修改n的值，继续执行while循环
                sleep(poll_frequency)
                n = n - 1
        # 超过最大询问次数还未定位到元素，返回None
        return None

    # 定位多个元素（含等待逻辑）
    def locate_elements(self, by, value, poll_frequency=0.2, timeout=5):
        locator = self.get_locator(by, value)
        elements = []
        # 最大询问次数
        n = timeout / poll_frequency
        while n > 0:
            # 定位多个元素
            elements = self.driver.find_elements(*locator)
            # 定位的多个元素不为空
            if elements:
                return elements
            # 定位的多个元素为空，程序睡眠0.2秒，继续循环定位元素
            sleep(poll_frequency)
            n -= 1
        return elements

    # 封装进入frame
    def switch_to_frame(self, by, value):
        iframe1 = self.locate_element(by,value)
        self.driver.switch_to.frame(iframe1)

    #封装退出frame
    def switch_to_parent(self):
        self.driver.switch_to.parent_frame()

    # 封装通过索引选择下拉项
    def select_by_index_self(self, by, value, index):
        select = self.locate_element(by, value)
        Select(select).select_by_index(index)

    # 封装通过value选择下拉项
    def select_by_value_self(self, by, value, select_value):
        select = self.locate_element(by, value)
        Select(select).select_by_value(select_value)

    # 封装通过文本选择下拉项
    def select_by_visible_text_self(self, by, value, text):
        select = self.locate_element(by, value)
        Select(select).select_by_visible_text(text)

    #封装截图
    def screen_shot(self,path,name):
        dt = datetime.now()
        timestamp = dt.strftime('%Y-%m-%d %H-%M-%S')
        filename=name+timestamp
        self.driver.save_screenshot(f"{path}/{filename}.png")

    #获取窗口句柄
    def get_handles(self):
        handles=self.driver.window_handles
        return handles

    #切换窗口句柄
    def switch_handles(self,handle):
        self.driver.switch_to.window(handle)

    #清空文本
    def clean_text(self,by, value):
        text=self.locate_element(by,value)
        text.clear()

    #后退
    def back_window(self):
        self.driver.back()

    #alert弹出框
    def alert(self):
        alert=self.driver.switch_to.alert
        alert.accept()