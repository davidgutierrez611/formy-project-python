#!/usr/bin/env python3

from selenium import webdriver;
import time

#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/dropdown")
time.sleep(3)

# Click the drop down menu
dropDown = driver.find_element_by_id("dropdownMenuButton")
dropDown.click()
time.sleep(3)

autocomplete = driver.find_element_by_id("autocomplete")
autocomplete.click()
time.sleep(3)


driver.quit()