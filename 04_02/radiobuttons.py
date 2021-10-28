from selenium import webdriver;
import time

#Launches the webdriver in this case chrome. Then goes to website
driver = webdriver.Chrome();

# Navigates to web address
driver.get("https://formy-project.herokuapp.com/radiobutton")
time.sleep(5)

# Click the first radio button using id
radioButton1 = driver.find_element_by_id("radio-button-1")
radioButton1.click()
time.sleep(2)


# Click on the second radio button using CSS Selector
radioButton2 = driver.find_element_by_css_selector(".form-check-input[value ='option2']")
radioButton2.click()
time.sleep(2)


#Click on the third radio button using XPath
radioButton3 = driver.find_element_by_xpath("/html/body/div/div[3]/input")
radioButton3.click()
time.sleep(2)

driver.quit()