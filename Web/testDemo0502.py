# coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_search():
    driver = webdriver.Chrome()
    # WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(By.TAG_NAME, 'title'))
    driver.get('https://www.baidu.com')
    search = driver.find_element_by_id('su').get_attribute('value')
    assert search == '百度一下'
