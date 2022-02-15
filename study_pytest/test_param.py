# coding:utf-8
import pytest

test_user_data = ['jerry', 'jack', 'tom']


@pytest.fixture(scope='module')
def login_r(request):
    user = request.param
    print(f"\n 登录用户名：{user}")
    return user


@pytest.mark.parametrize('login_r', test_user_data, indirect=True)
def test_login(login_r):
    print(f"测试用例中login的返回值：{login_r}")
    assert login_r != ''


@pytest.mark.parametrize("x", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
@pytest.mark.parametrize("y", [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])
def test_too(x, y):
    print(f"测试数据组合是x:{x},y:{y}")
