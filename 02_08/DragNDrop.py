from selenium import webdriver;
import time
from selenium.webdriver.common.action_chains import ActionChains

#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/dragdrop")

# Finds the image
image = driver.find_element_by_id("image")

# Find the box
box = driver.find_element_by_id("box")

# ActionChains to drag and drop
actions = ActionChains(driver)
actions.drag_and_drop(image, box).perform()

time.sleep(3)

driver.quit()