# -*-coding:utf-8-*-
__author__ = 'YL'

import yaml
from behave import Step


class TestCaseStore:
    def __init__(self):
        self.test_params = {}
        self.testcase = {}

    def load(self, path):
        with open(path) as f:
            methods = yaml.load(f)
        step_method = []
        for method_name, steps in methods.items():
            for step in steps:
                step_method.append(Step(step))
            if method_name.startswith('test_'):
                self.test_params[method_name] = step_method
        self.testcase_gen()

    def testcase_gen(self):
        self.testcase = self.test_params
