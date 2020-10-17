# -*- coding: utf-8 -*-

##模块级别,每一个py文件前后
def setup_module():
    print("资源准备：setup_module")


def teardown_module():
    print("资源销毁：teardown_module")


def test_case1():
    print("case1")


# 每个方法的前后
def setup_function():
    print("资源准备：setup_function")


def teardown_function():
    print("资源销毁：teardown_functiion")


class TestDemo:
    # 每个类的前后
    def setup_class(self):
        print("class setup")

    def teardown_class(self):
        print("class teardown")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def setup_function(self):
        print("资源准备：setup_function")

    def teardown_function(self):
        print("资源销毁：teardown_functiion")

    def test_dmeo1(self):
        print("test Demo1")

    def test_dmeo2(self):
        print("test Demo2")


class TestDemo1:
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test_dmeo1(self):
        print("test Demo1")

    def test_dmeo2(self):
        print("test Demo2")
