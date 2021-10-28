#!/usr/bin/env python3
from selenium import webdriver;
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/form")
time.sleep(2)

# Send first name
driver.find_element_by_id("first-name").send_keys("David")
time.sleep(2)

# Send last name.
driver.find_element_by_id("last-name").send_keys("Gutierrez")
time.sleep(2)

# Send job title keys
driver.find_element_by_id("job-title").send_keys("Engineer")
time.sleep(2)

# Select education on radio button
driver.find_element_by_id("radio-button-2").click()
time.sleep(2)

# Selecting gender.
driver.find_element_by_id("checkbox-1").click()
time.sleep(2)

# Selecting of work experience year.
driver.find_element_by_css_selector("option[value ='2']").click()
time.sleep(2)

# Choosing date.
driver.find_element_by_id("datepicker").send_keys("10/28/2021")
driver.find_element_by_id("datepicker").send_keys(Keys.RETURN)
time.sleep(2)

# Selecting submit button
driver.find_element_by_css_selector(".btn.btn-lg.btn-primary").click()
time.sleep(2)

# Verify that the successful banner is presented
wait = WebDriverWait(driver, 10)
alert = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))

# Verify the banner is correct
alertText = alert.text
assert alertText == "The form was successfully submitted!" , "Incorrect text captured"
print(alertText)

driver.quit()

