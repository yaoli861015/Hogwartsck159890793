# -*-coding:utf-8-*-
__author__ = 'YL'

import allure
import pytest


@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤1，打开应用"):
            print("打开应用")
        with allure.step("步骤2，启动程序"):
            print("启动程序")
        print("登录成功")

    @allure.story("登录失败")
    def test_login_fail(self):
        print("登录失败")

    @allure.story("登录用户名缺失")
    def test_login_lose_user_name(self):
        print("登录缺失用户名")

    @allure.story("登录密码缺失")
    def test_login_lose_password(self):
        print("登录缺失密码")
