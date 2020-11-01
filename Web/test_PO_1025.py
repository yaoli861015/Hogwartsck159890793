# -*-coding:utf-8-*-
__author__ = 'YL'

from selenium import webdriver


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
