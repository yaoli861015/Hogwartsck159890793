# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class TestHogwarts():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://home.testing-studio.com/')
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_hogwarts(self):
        category_name = (By.CSS_SELECTOR, '#ember195 .category-name')
        self.driver.find_element_by_partial_link_text('分类').click()
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(category_name))
        self.driver.find_element(*category_name).click()
