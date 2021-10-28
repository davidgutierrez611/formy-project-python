from selenium import webdriver;
import time


#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/modal")

time.sleep(2)

modal = driver.find_element_by_id("modal-button")
modal.click()

time.sleep(3)

# Find close button in modal and use javascript to close
close_button = driver.find_element_by_id("close-button")
driver.execute_script("arguments[0].click()", close_button)

time.sleep(3)
driver.quit()