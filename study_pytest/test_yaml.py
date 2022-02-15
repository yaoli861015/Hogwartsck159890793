# coding:utf-8

import pytest
import yaml

f = open('data.yaml', 'r', encoding='utf8')
datas = yaml.safe_load(f)


# file = open('data.yaml')
# datas = yaml.safe_load(file)

#
# @pytest.mark.parametrize('a,b', datas)
# def test_foo(a, b):
#     print(datas)
#     print('a+b的值是:', a + b)


def test_yaml_read():
    with open('data.yaml', 'r', encoding='utf8') as f:
        print(yaml.load(f.read(), Loader=yaml.FullLoader))


if __name__ == '__main__':
    test_yaml_read()
