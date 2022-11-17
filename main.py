import time
from datetime import datetime, date, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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

# Creates a list of available Tee Times
teeTimes = driver.find_elements("xpath", "//li[contains(@class, 'reservation-group-item')]")
print(teeTimes)

# Scrolls the page down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(5)

# Prints all the available tee times
for teeTime in teeTimes:
  print(teeTime.get_attribute("innerHTML"))


