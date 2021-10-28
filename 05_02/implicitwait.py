#!/usr/bin/env python3
from selenium import webdriver;
import time

#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/autocomplete")
time.sleep(3)

autocomplete = driver.find_element_by_id("autocomplete")
autocomplete.send_keys("206 N Flora Pkwy, Addison, IL")
driver.implicitly_wait(5)

autocompleteResult = driver.find_element_by_class_name("pac-item")
autocompleteResult.click()
time.sleep(5)

driver.quit()