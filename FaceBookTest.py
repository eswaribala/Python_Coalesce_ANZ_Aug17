# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class FaceBookTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.facebook.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_face_book(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("Parameswaribala@gmail.com")
        driver.find_element_by_id("pass").clear()
        driver.find_element_by_id("pass").send_keys("vigneshbala95")
        driver.find_element_by_id("u_0_0").click()
        driver.find_element_by_id("userNavigationLabel").click()
        driver.find_element_by_id("userNavigationLabel").click()
        driver.find_element_by_id("userNavigationLabel").click()
        #driver.find_element_by_xpath("//div[@id='js_1g']/div/div/ul/li[16]/a/span/span").click()
        driver.close()
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
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
        #self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
