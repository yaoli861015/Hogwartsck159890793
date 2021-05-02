# -*-coding:utf-8-*-
__author__ = 'YL'

from selenium import webdriver
import time


def test_selenium():
    # global driver
    # chromedriver_path = r"D:\chromedriver\chromedriver.exe"
    # driver = webdriver.Chrome(executable_path=chromedriver_path)
    global driver
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    time.sleep(10)
    driver.quit()


if __name__ == '__main__':
    test_selenium()
