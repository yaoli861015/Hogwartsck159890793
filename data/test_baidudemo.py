# coding:utf-8

import allure
import pytest
import yaml
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

file = open('data.yaml')
datas = yaml.safe_load(file)


@allure.testcase('http:www.github.com')
@allure.feature('百度搜索')
@pytest.mark.parametrize('test_data1', datas)
def test_steps_demo(test_data1):
    with allure.step('百度搜索'):
        driver = webdriver.Chrome()
        driver.get('https:www.baidu.com')
        driver.maximize_window()
        time.sleep(3)

    with allure.step(f'输入搜索词：{test_data1}'):
        driver.find_element(by=By.ID, value='kw').send_keys(test_data1)
        time.sleep(2)
        driver.find_element(by=By.ID, value='su').click()
        time.sleep(3)

    with allure.step('保存图片'):
        driver.save_screenshot('./result/b.png')
        allure.attach.file('./result/b.png', attachment_type=allure.attachment_type.PNG)

    with allure.step('关闭浏览器'):
        driver.quit()
