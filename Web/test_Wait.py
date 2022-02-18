# coding:utf - 8
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.ceshiren.com")
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        time.sleep(1)
        self.driver.quit()

    def test_hogwarts(self):
        category_name = (By.XPATH, "//*[normalize-space(text())='开源项目交流与维护']")
        self.driver.find_element_by_link_text('开源项目').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(category_name))
        self.driver.find_element(*category_name).click()
        time.sleep(10)
