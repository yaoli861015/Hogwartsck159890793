# -*- coding: utf-8 -*-
from decimal import *

# 测试代码（加减乘除）
import pytest


@pytest.mark.parametrize
def test_div1(a, b):
    if b != 0:
        return Decimal(a / b).quantize(Decimal('0.00'))
    else:
        raise Exception("分母不能为零")


class Calculator:
    # 加法
    def add(self, a, b):
        return round((a + b), 2)

    # 减法
    def sub(self, a, b):
        return a - b

    # 乘法
    def mul(self, a, b):
        return a * b

    # 除法
    def test_div(self, a, b):
        if b != 0:
            return round(a / b, 2)
        else:
            raise Exception("分母不能为零")
