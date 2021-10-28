#!/usr/bin/env python3


from selenium import webdriver;
import time

#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/fileupload")
time.sleep(3)

# Click the file upload
fileUpload = driver.find_element_by_id("file-upload-field")
fileUpload.send_keys("file-to-upload.png")
time.sleep(5)


driver.quit()