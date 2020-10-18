# -*-coding:utf-8-*-
__author__ = 'YL'

import pytest


@pytest.fixture()
def login():
    print("login成功")
    yield
    print("退出登录")


def db_conn():
    print("数据库连接")
    yield ["tom", "123456"]
    print("数据库断开连接")


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escapw')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
