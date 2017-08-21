# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 20:18:20 2017

@author: BALASUBRAMANIAM
"""
import requests
from bs4 import BeautifulSoup
page = requests.get("http://www.thehindu.com/")
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#finding only paragraphs
#print(soup.find_all('p'))
#finding only paragraph text
#print(soup.find_all('p')[0].get_text())
#finding only paragraph class
#print(soup.find_all('p', class_='hidden-xs'))

#print(soup.select("div p"))






'''
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

print(period)
print(short_desc)
print(temp)
'''
req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)', verify=True)
soup = BeautifulSoup(req.text, "lxml")
print(soup.title)
print(soup.title.name)
print(soup.p.contents)


