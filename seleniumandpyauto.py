'''
Created on 21-Aug-2017

@author: BALASUBRAMANIAM
'''
import datetime
import time

import pyautogui
from selenium import webdriver


while True:
    print(datetime.datetime.now())
    try:
        # Firefox ain't got no Flash
        browser = webdriver.Firefox()
        browser.maximize_window()
        # drop the pleasantries, just open the Flash object
        browser.get('http://speedtest1.rcs-rds.ro/netgauge.swf?v=3.0')
        # wait for the page to load
        #time.sleep(1 * 60)
        # make sure the browser is in focus
        browser.maximize_window()
        #time.sleep(1 * 60)
        # click the start test button
        pyautogui.moveTo(683, 333)
        #pyautogui.alert('This displays some text with an OK button.')
        pyautogui.doubleClick()
        # wait for the test to finish
        time.sleep(1 * 2)
        browser.save_screenshot(datetime.datetime.now().strftime('rds__%Y-%m-%d__%H.%M.png'))
        browser.close()
        #time.sleep(5 * 60)
    except Exception as e:
        print (e.message)