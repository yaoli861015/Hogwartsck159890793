# -*-coding:utf-8-*-
__author__ = 'YL'

import pytest


@pytest.mark.parametrize('a', [4, 5, 6])
@pytest.mark.parametrize('b', [7, 8, 9])
@pytest.mark.parametrize('c', [1, 2, 3])
def test_parm(a, b, c):
    print(a + b + c)


@pytest.mark.parametrize("a,b", [(20, 30), (3, 6), (0.1, 0.4)])
def test_param(a, b):
    print(a + b)
