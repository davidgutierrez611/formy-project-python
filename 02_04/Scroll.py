from selenium import webdriver;
import time

# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains


#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/scroll")

time.sleep(2)

name = driver.find_element_by_id("name")

# create action chain object
action = ActionChains(driver)
action.move_to_element(name)
name.send_keys("David Gutierrez")


date = driver.find_element_by_id("date")
date.send_keys("10/06/2021")

time.sleep(5)

driver.quit()