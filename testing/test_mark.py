# -*-coding:utf-8-*-
__author__ = 'YL'

import pytest


@pytest.mark.login
def test_login():
    print("登录测试")


@pytest.mark.login
def test_login2():
    print("登录2")


def test_search1():
    print("搜索用例1")


def test_search2():
    print("搜索用例2")
