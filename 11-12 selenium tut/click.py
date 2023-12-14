from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = 'standard_user'
password = 'secret_sauce'

driver = webdriver.Chrome()
# write a selenium script to open https://www.saucedemo.com/ and wait for 3 sec
# open the window in maximized mode

driver.maximize_window()
driver.get('https://www.saucedemo.com/')
time.sleep(3)

# declare a new variable which represent the element div form the html website
# using the css selector and call the var - swag_label
swag_label = driver.find_element(By.CSS_SELECTOR, '#root > div > div.login_logo')
# print the text from the website
print(swag_label.text)

# declare a new variable which represent the input element by css selector
username_input = driver.find_element(By.CSS_SELECTOR, '#user-name')
# this function takes str and send it to the website as input
username_input.send_keys(username)

# enter the password for the user 'secret_sauce'
password_input = driver.find_element(By.CSS_SELECTOR, '#password')
password_input.send_keys(password)

login_btn = driver.find_element(By.CSS_SELECTOR, '#login-button')
login_btn.click()

time.sleep(5)
if driver.current_url == 'https://www.saucedemo.com/inventory.html':
    print('login test pass')
else:
    print('login test fail')
driver.close()
