# coding:utf-8
import time

from selenium import webdriver


def test_steps_demo():
    driver = webdriver.Chrome()
    driver.get("https:www.baidu.com")
