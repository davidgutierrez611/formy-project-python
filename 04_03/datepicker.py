#!/usr/bin/env python3

from selenium import webdriver;
import time
from selenium.webdriver.common.keys import Keys

#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/datepicker")
time.sleep(3)

# Select the datepicker
datePicker = driver.find_element_by_id("datepicker")
datePicker.send_keys("10/14/2022")
datePicker.send_keys(Keys.RETURN)
time.sleep(5)


driver.quit()