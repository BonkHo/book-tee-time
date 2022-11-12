from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import pause
from datetime import datetime

# Script does not start until 9AM
#pause until(datetime(2020, 12, 7, 9 0))
gotwed = False
gotsat = False
count = 0

# Opening Chrome and inputs ID and Password
browser = webdriver.Chrome('/usr/local/bin')
browser.get('https://letsgo.golf/los-verdes-golf-course/teeTimes/los-verdes-golf-course-california?date=2022-11-11')
idbar = browser.find_element_by_id('ctl00_Content_UserID')
idbar.send_keys('id')
pwbar = browser.find_element_by_id('ctl100_Content_UserPassword')
pwbar.send_keys('pw')
pwbar.send_keys(Keys.ENTER)

# Searches for the element and clicks and confirms. time.sleep(5) prevents timeout errors
def reserveseq():
  confirm = browser.find_element_by_xpath('HTML ELEMENT')
  confirm.click()
  time.sleep(5)
  browser.switch_to_alert().accept()
  time.sleep(5)
  browser.switch_to_alert().accept()

def entirereserve(day):
  table = browser.find_elements_by_xpath('HTML ELEMENT')
  numberOfRows = len(table)
  print(numberOfRows)
  noneString = browser.find_element_by_xpath('HTML ELEMENT')
  global gotwed
  global gotsat
  if noneString == 'FAILURE MESSAGE':
      print ('Not Available')
  else:
    for i in range(1, numberOfRows + 1):
      tableString = "HTML PATH FOR EACH ROW OF TABLE"
      potentialTime = browser.find_element_by_xpath(tableString).text
      print(potentialTime)
      if 'PREFERRED TIME' in potentialTime or 'PREFERRED TIME' in potentialTime:
        iterButtonString = 'HTML PATH FOR ROW OF TABLE'
        
