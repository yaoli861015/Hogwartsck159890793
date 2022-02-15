# coding:utf-8
import pytest


@pytest.fixture(scope='module')
def open_windows():
    print('打开浏览器')
    yield
    print('执行teardown!!!')
    print('最后关闭浏览器')


def test_search1(open_windows):
    print('test_search1')
    raise Exception('出错了')
    pass


def test_search2(open_windows):
    print('test_search2')


def test_search3(open_windows):
    print('test_search3')
    pass


@pytest.mark.usefixtures('open_windows')
def test_search4(open_windows):
    print('test_search4')
    pass
