# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Untitled3(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/php4dvd/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled3(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("sample3")
        driver.find_element_by_name("aka").clear()
        driver.find_element_by_name("aka").send_keys("sample")
        driver.find_element_by_name("year").click()
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("1999")
        driver.find_element_by_name("duration").clear()
        driver.find_element_by_name("duration").send_keys("100")
        driver.find_element_by_name("rating").clear()
        driver.find_element_by_name("rating").send_keys("5")
        driver.find_element_by_id("own_no").click()
        driver.find_element_by_id("seen_no").click()
        driver.find_element_by_id("loaned_yes").click()
        driver.find_element_by_name("rating").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("qwerty")
        driver.find_element_by_name("taglines").clear()
        driver.find_element_by_name("taglines").send_keys("qwerty")
        driver.find_element_by_name("plotoutline").clear()
        driver.find_element_by_name("plotoutline").send_keys("qwerty")
        driver.find_element_by_name("plots").clear()
        driver.find_element_by_name("plots").send_keys("sample plot")
        driver.find_element_by_id("text_languages_0").clear()
        driver.find_element_by_id("text_languages_0").send_keys("lang1")
        driver.find_element_by_name("subtitles").clear()
        driver.find_element_by_name("subtitles").send_keys("no")
        driver.find_element_by_name("audio").clear()
        driver.find_element_by_name("audio").send_keys("yes")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]")
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
