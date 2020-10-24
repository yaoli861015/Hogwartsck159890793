# -*-coding:utf-8-*-
__author__ = 'YL'

from testing.conftest import login, db_conn


def test_case1(c):
    print("测试case1")


def test_case2(db_conn):
    print("测试case2")


def test_case3(login, db_conn):
    print("测试case3")
