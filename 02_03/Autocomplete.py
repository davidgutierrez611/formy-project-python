from selenium import webdriver;
import time

#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/autocomplete")

time.sleep(2)


autocomplete = driver.find_element_by_id("autocomplete")
autocomplete.send_keys("1120 Blackhawk Dr, Elgin, IL 60120")

time.sleep(5)

autocomplete_result = driver.find_element_by_class_name("pac-item")
autocomplete_result.click()

time.sleep(5)

driver.quit()