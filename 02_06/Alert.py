from selenium import webdriver;
import time

# import Alert 
from selenium.webdriver.common.alert import Alert


#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/switch-window")

time.sleep(2)

# clicks on alert button
alert_button = driver.find_element_by_id("alert-button")
alert_button.click()

time.sleep(2)

# Handling an alert
alert = driver.switch_to.alert
alert.accept()

time.sleep(3)

driver.quit()