# coding:utf-8


import pytest


@pytest.fixture(params=[1, 2, 3, 4, 5])
def data(request):
    return request.param


def test_param2(data):
    print(f'测试数据{data}')
    assert data >= 1
