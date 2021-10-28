from selenium import webdriver;
import time


#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/switch-window")

time.sleep(2)

# clicks on tab button
tab_button = driver.find_element_by_id("new-tab-button")
tab_button.click()

time.sleep(3)

# Get original tab
original_tab = driver.current_window_handle


# Switch to second tab
for handle1 in driver.window_handles:
	driver.switch_to.window(handle1)

time.sleep(5)

# Go back to original tab. 
driver.switch_to.window(original_tab)

time.sleep(5)

driver.quit()