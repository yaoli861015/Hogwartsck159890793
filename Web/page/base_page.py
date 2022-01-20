# coding=utf-8

from time import sleep
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
            self._driver.get(self._base_url)
        else:
            self._driver = driver

    def close(self):
        sleep(20)
        self._driver.quit()
