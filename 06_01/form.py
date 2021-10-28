#!/usr/bin/env python3
from selenium import webdriver;
import time
from selenium.webdriver.common.keys import Keys

#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/form")
time.sleep(3)

# Send first name
driver.find_element_by_id("first-name").send_keys("David")
time.sleep(3)

# Send last name.
driver.find_element_by_id("last-name").send_keys("Gutierrez")
time.sleep(3)

# Send job title keys
driver.find_element_by_id("job-title").send_keys("Engineer")
time.sleep(3)

# Select education on radio button
driver.find_element_by_id("radio-button-2").click()
time.sleep(3)

# Selecting gender.
driver.find_element_by_id("checkbox-1").click()
time.sleep(3)

# Selecting of work experience year.
driver.find_element_by_css_selector("option[value ='2']").click()
time.sleep(3)

# Choosing date.
driver.find_element_by_id("datepicker").send_keys("10/28/2021")
driver.find_element_by_id("datepicker").send_keys(Keys.RETURN)
time.sleep(3)

# Selecting submit button
driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
time.sleep(3)

driver.quit()