# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled6(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/php4dvd/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled6(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_id("imdbsearch").clear()
        driver.find_element_by_id("imdbsearch").send_keys("new")
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("new_search")
        driver.find_element_by_name("year").click()
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("2025")
        driver.find_element_by_id("submit").click()
        driver.find_elements_by_xpath("//*[contains(text(), 'new_search')]")
        driver.find_element_by_css_selector("h1").click()
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("new_search")
        driver.find_element_by_id("q").click()
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        driver.find_elements_by_xpath("//*[contains(text(), 'new_search')]")
        driver.find_element_by_css_selector("div.nocover").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
        self.assertFalse(self.is_element_present(By.LINK_TEXT, "new_search"))
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
