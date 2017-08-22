'''
Created on 21-Aug-2017

@author: BALASUBRAMANIAM
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 
 
def init_driver():
    driver = webdriver.Edge()
    driver.wait = WebDriverWait(driver, 5)
    return driver
 
 
def lookup(driver, query):
    driver.get("https://www.google.co.in/?gfe_rd=cr&ei=MhKbWcCyNIvy8Aegw47IAw&gws_rd=ssl")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "q")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "btnK")))
        box.send_keys(query)
        button.submit()
    except TimeoutException:
        print("Box or Button not found in google.com")
 
 
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver, "Selenium")
    time.sleep(5)
    driver.quit()