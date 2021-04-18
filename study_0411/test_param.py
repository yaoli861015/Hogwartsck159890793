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
