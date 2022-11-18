import time
import os
from dotenv import load_dotenv
from datetime import datetime, date, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Loads data from the .env file for username and password
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Initialize options for Web Driver
options = Options()
options.add_experimental_option("detach", True)

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

# Signs into the account
signIn = driver.find_element("xpath", "//a[contains(concat(' ',normalize-space(@class),' '),' top-bar__margined ')]")
signIn.click()
time.sleep(3)
emailField = driver.find_element("xpath", "//input[@id='email']")
passwordField = driver.find_element("xpath", "//input[@id='password']")
emailField.send_keys(username)
passwordField.send_keys(password)
logInButton = driver.find_element("xpath", "//button[contains(concat(' ',normalize-space(@class),' '),' submit-button ')]")
logInButton.click()

time.sleep(5)

# Creates a list of available Tee Times
teeTimes = driver.find_elements("xpath", "//span[contains(concat(' ',normalize-space(@class),' '),' start-time ')]")

# Clicks on the first available Tee Time
teeTimes[0].click()

print("Completed")