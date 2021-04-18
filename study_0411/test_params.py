# coding:utf-8


import pytest

lista = []
for i in range(1, 100):
    lista.append(i)

print(lista)


@pytest.fixture(params=lista)
def data(request):
    return request.param


def test_param2(data):
    print(f'测试数据{data}')
    assert data >= 1


@pytest.mark.parametrize("test_input,excepted", [("3+5", 8), ("2+5", 7), ("3+4", 7), ("5*5", 30)])
def test_eval(test_input, excepted):
    assert eval(test_input) == excepted


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]


@pytest.mark.parametrize("x", a)
@pytest.mark.parametrize("y", b)
def test_foo(x, y):
    print(f'测试数据的组合x：{x},y:{y}')
