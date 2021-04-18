# coding:utf-8

import pytest
import yaml

file = open('data.yaml')
datas = yaml.safe_load(file)


@pytest.mark.parametrize('a,b', datas)
def test_foo(a, b):
    print(f'a+b = {a, b}')
