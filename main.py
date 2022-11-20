import time
import os
import pickle
from dotenv import load_dotenv
from datetime import datetime, date, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

# Loads data from the .env file for username and password
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Initialize options for Web Driver
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("/Applications/Google Chrome.app")
service = Service(ChromeDriverManager().install())


# Initialize the Web Driver and set options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Initialize current Date and bookDate
today = date.today()
bookDate = today + timedelta(days=9)

# Creates and stores link needed
link = "https://letsgo.golf/los-verdes-golf-course/teeTimes/los-verdes-golf-course-california?date="
link += bookDate.strftime("%Y-%m-%d")

# Opens webpage and maximizes the window
driver.get(link)
driver.maximize_window() 

# Load Cookies
try:
  cookie = pickle.load(open("cookie.pkl", "rb")) #loading from pickle file
  for i in cookie:
      driver.add_cookie(i)
  print('Cookies added.')
except Exception as e:
  print(e)

# Signs into the account
# signIn = driver.find_element("xpath", "//a[contains(concat(' ',normalize-space(@class),' '),' top-bar__margined ')]")
# signIn.click()
# time.sleep(3)
# emailField = driver.find_element("xpath", "//input[@id='email']")
# passwordField = driver.find_element("xpath", "//input[@id='password']")
# emailField.send_keys(username)
# passwordField.send_keys(password)
# rememberMeCheck = driver.find_element("xpath", "//label[contains(concat(' ',normalize-space(@class),' '),' custom-control-label ')]")
# rememberMeCheck.click()
# logInButton = driver.find_element("xpath", "//button[contains(concat(' ',normalize-space(@class),' '),' submit-button ')]")
# logInButton.click()

time.sleep(4)

# Creates a list of available Tee Times
playerCountButton = driver.find_element("xpath", "//div[contains(concat(' ',normalize-space(@class),' '),' Rectangle-Player-13 ')]")
playerCountButton.click()
time.sleep(1)
optionFour = driver.find_element("xpath", "//div[@id='react-select-Players-option-4']")
optionFour.click()
searchButton = driver.find_element("xpath", "//div/img[contains(concat(' ',normalize-space(@class),' '),' search-btn-img ')]")
searchButton.click()
time.sleep(3)

teeTimes = driver.find_elements("xpath", "//span[contains(concat(' ',normalize-space(@class),' '),' start-time ')]")


# Clicks on the first available Tee Time
# acceptableTimes = ["12:00 PM","12:10 PM", "12:20 PM","12:30 PM"]
# for teeTime in teeTimes:
#   if teeTime.get_attribute("innerHTML") in acceptableTimes:
#     teeTime.click()
#     break

teeTimes[0].click()

time.sleep(3)

# Clicks on the Public Tee Time Listings
publicTimesListings = driver.find_element("xpath", "//h3[contains(concat(' ',normalize-space(@class),' '),' mr-price ')]")
publicTimesListings.click()

time.sleep(4)

# Change reservation to 4 people and finish reservation
cardCheckBox = driver.find_element("xpath", "//div[contains(concat(' ',normalize-space(@class),' '),' custom-radio ')]")
termsConditionsBox = driver.find_element("xpath", "//div[contains(concat(' ',normalize-space(@class),' '),' custom-checkbox ')]")
cardCheckBox.click()
termsConditionsBox.click()

# Save cookies
# try:
#   pickle.dump(driver.get_cookies(), open("cookie.pkl", "wb")) #writing in pickle file
#   print('Cookie file successfully created.')
# except Exception as e:
#   print(e)

print("Completed")