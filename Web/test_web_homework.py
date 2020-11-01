# -*-coding:utf-8-*-
__author__ = 'YL'

import shelve

from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.options import Options


class TestWebQQ1022:
    # global driver
    def setup(self):
        options = Options()
        # options.binary_location = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe"
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    # def test_demo(self):
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     pass

    def test_login_and_get_cookie(self):
        # db = shelve.open("cookiesdata")
        # cookies = db["cookie"]
        # db.close()

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print(cookie)
            self.driver.add_cookie(cookie)
        self.driver.refresh()
