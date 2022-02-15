# coding = utf-8
def setup_module():
    print('\nsetup_module,只执行一次，当有多个测试类的时候使用')


def teardown_module():
    print('\nteardown_module,只执行一次，当有多个测试类的时候执行')


class TestPytest1:
    @classmethod
    def setup_class(cls):
        print('\nsetup_class1,只执行一次')

    @classmethod
    def teardown_class(cls):
        print('\nteardown_class1,只执行一次')

    def setup_method(self):
        print('\nsetup_method,在每个测试方法开始时先调用，都执行一次')

    def teardown_method(self):
        print('\nteardown_method,在每个测试方法结束后调用，都只执行一次')

    def test_three(self):
        print('test_three,测试用例3')

    def test_four(self):
        print('test_four,测试用例4')


class TestPytest2:
    @classmethod
    def setup_class(cls):
        print('\nsetup_class2,只执行一次')

    @classmethod
    def teardown_class(cls):
        print('\nteardown_class2,只执行一次')

    def setup_method(self):
        print('\nsetup_method2,在每个测试方法开始时先调用，都执行一次')

    def teardown_method(self):
        print('\nteardown_method2,在每个测试方法结束后调用，都只执行一次')

    def test_one(self):
        print('test_one,测试用例1')

    def test_two(self):
        print('two,测试用例2')

    def test_s(self):
        print('two,测试用例3')

    def test_d(self):
        print('two,测试用例4')

    def test_f(self):
        print('two,测试用例5')

    def test_e(self):
        print('two,测试用例6')
