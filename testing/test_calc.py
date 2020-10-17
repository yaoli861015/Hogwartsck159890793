# -*- coding: utf-8 -*-
from pythoncode.calculator import Calculator


class TestCalc():
    calc = Calculator()

    def setup_class(self):
        print("计算开始")
        # self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    def test_add(self):
        result = self.calc.add(1, 1)
        assert result == 2

    def test_sub(self):
        result = self.calc.sub(3, 1)
        assert result == 2

    def test_mul(self):
        result = self.calc.mul(3, 3)
        assert result == 9

    def test_div(self):
        result = self.calc.div(3, 1)
        assert result == 3
