from selenium import webdriver;
import time

#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/keypress")

time.sleep(2)

# Find the element to input name
name = driver.find_element_by_id("name")
name.click()
name.send_keys("David Gutierrez")

time.sleep(5)

# Find the element to click the button.
button = driver.find_element_by_id("button")
button.click()

time.sleep(5)

driver.quit()