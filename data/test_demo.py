# coding:utf-8
import time

import pytest
from selenium import webdriver

test_user_data = ["tom", "jerry"]


@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"\n登录的用户名：{user}")
    return user


@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"测试用例中login返回的值是：{a}")
    assert a != ''
