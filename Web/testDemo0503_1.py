# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


def test_baidu():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    search = driver.find_element_by_id('su')
    print(search.get_attribute('value'))
    print(search.location)
    print(search.size)
    driver.refresh()
    # print(driver.page_source)
    driver.minimize_window()
    driver.maximize_window()
    driver.set_window_size(1000, 1000)
