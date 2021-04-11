# coding:utf-8
import pytest


class TestPytestOrder:
    @pytest.mark.run(order=3)
    def test_one(self):
        print('测试用例1')

    @pytest.mark.run(order=1)
    def test_two(self):
        print('测试用例2')

    @pytest.mark.run(order=0)
    def test_three(self):
        print('测试用例3')

    @pytest.mark.run(order=2)
    def test_four(self):
        print('测试用例4')
