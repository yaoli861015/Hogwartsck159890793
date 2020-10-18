# -*-coding:utf-8-*-
__author__ = 'YL'

from testing.conftest import login, db_conn


def test_case1(login):
    print("测试case1")


def test_case2():
    print("测试case2")


def test_case3():
    print("测试case3")
    print(login)
    print(db_conn)
