# coding = utf-8

from selenium.webdriver.common.by import By
from Web.page.base_page import BasePage
from Web.page.register import RegisterPage


class Login(BasePage):
    def scan_qrcode(self):
        pass

    # 进入到注册页面
    def goto_register_view(self):
        self._driver.find_element(By.LINK_TEXT, '企业注册').click()
        return self
