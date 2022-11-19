from datetime import time

from selenium import webdriver

# browser exposes an executable file
# Through Selenium test we will invoke the executable file which will then #invoke actual browser
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="../chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
# get method to launch the URL
driver.get("https://pwhr.darwinbox.in/user/login")

driver.find_element(By.ID, "UserLogin_username").send_keys("PW2235")
driver.find_element(By.ID, "UserLogin_password").send_keys("Raghu@22")
driver.find_element(By.ID, "login-submit").click()
# driver.find_element(By.ID, "attendance-logger-widget").click()

time.sleep(5)
driver.close()