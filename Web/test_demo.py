# -*-coding:utf-8-*-
__author__ = 'YL'

from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_selenium():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com/')
    search = driver.find_element(value='su').get_attribute('value')
    assert search == '百度一下'
    driver.quit()


def test_action():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.refresh()
    print(driver.page_source)
    search = driver.find_element_by_id('su')
    print(search.get_attribute('value'))
    print(search.location)
    print(search.size)
    driver.close()
    driver.quit()
