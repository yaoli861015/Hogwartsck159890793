# -*- coding: utf-8 -*-
import pytest
from decimal import Decimal


from pythoncode.calculator import Calculator


class TestCalc():
    # calc = Calculator()

    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,c',
                             [[1, 1, 2],
                              [100, 100, 200],
                              [0.1, 0.1, 0.2],
                              [-1, -2, -3],
                              [1, 0, 1]], ids=['int_case', 'bigNum_case', 'float_case', 'minus_case', 'zero_case'])
    def test_add(self, a, b, c):
        result = self.calc.add(a, b)
        assert result == c

    def test_add1(self):
        test_data = [[1, 2, 3], [100, 1000, 1100], [0.56, 0.67, 1.23], [-3, -4.5, -7.5], [0, 3, 3]]
        # print (test_data[1])
        for i in range(0, len(test_data)):
            result = self.calc.add(test_data[i][0], test_data[i][1])
            assert result == test_data[i][2]

    def test_sub(self):
        result = self.calc.sub(3, 1)
        assert result == 2

    def test_mul(self):
        result = self.calc.mul(3, 3)
        assert result == 9

    ##方法round
    @pytest.mark.parametrize('e,d,f',
                             [[4, 2, 2.00],
                              [0.1, 0.1, 1.00],
                              [0, 5, 0],
                              [1, 0, 3],
                              [1, 3, 0.33],
                              [2, 3, 0.67]], ids=[u'整数相处', u'小数相除', u'分子为零', u'分母为零', u'不四舍五入', u'四舍五入'])
    def test_div(self, e, d, f):
        result = self.calc.div(e, d)
        assert result == f

    ##Decimal
    @pytest.mark.parametrize('e,d,f',
                             [[4, 2, 2.00],
                              [0.1, 0.1, 1.00],
                              [0, 5, 0],
                              [1, 0, 3],
                              [1, 3, 0.33],
                              [2, 3, 0.67]], ids=[u"整数相处", u"小数相除", u'分子为零', u'分母为零', u'不四舍五入', u'四舍五入'])
    def test_div(self, e, d, f):
        result = self.calc.div1(e, d)
        assert result == Decimal(f).quantize(Decimal('0.00'))
