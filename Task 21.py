from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the webdriver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://www.saucedemo.com/")

# Display cookies before login
print("Cookies before login:")
print(driver.get_cookies())

# Find and fill the username field
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

# Find and fill the password field
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("secret_sauce")

# Click the login button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Wait for the login to complete
time.sleep(3)

# Display cookies after login
print("Cookies after login:")
print(driver.get_cookies())

# Perform logout
menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
menu_button.click()
time.sleep(1)

logout_button = driver.find_element(By.ID, "logout_sidebar_link")
logout_button.click()

# Wait for the logout to complete
time.sleep(3)

# Display cookies after logout
print("Cookies after logout:")
print(driver.get_cookies())

# Close the browser
driver.quit()
