# coding:utf-8
import allure
from selenium import webdriver


@allure.feature("测试登录功能")
class TestLogin:
    @allure.story("测试成功的登录场景")
    def test_login(self):
        print(f"登录成功")
        pass

    @allure.story("测试失败的登录场景")
    def test_login2(self):
        print(f"登录失败")
        pass


@allure.step
def login():
    pass


@allure.step
def search():
    pass


def test_login_search_steps():
    login()
    search()


def test_search():
    with allure.step("打开chrome浏览器"):
        driver = webdriver.Chrome()
    with allure.step("打开Baidu。com"):
        driver.get("https:www.baidu.com")
