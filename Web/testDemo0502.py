# coding=utf-8

from selenium import webdriver


def test_search():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    search = driver.find_element_by_id('su').get_attribute('value')
    assert search == '百度一下'
