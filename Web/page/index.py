# coding = utf-8

from selenium.webdriver.common.by import By

from Web.page.base_page import BasePage
from Web.page.login import LoginPage
from Web.page.register import RegisterPage


class IndexPage(BasePage):
    _base_url = 'https://work.weixin.qq.com/'

    def go_to_register_view(self):
        self._driver.find_element(By.LINK_TEXT, '立即注册').click()
        return self

    def goto_login_view(self):
        self._driver.find_element(By.LINK_TEXT, '企业登录').click()
        return self
