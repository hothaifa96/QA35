from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.saucedemo.com/'

driver = webdriver.Chrome()

driver.maximize_window()

driver.get(url)

if driver.current_url == url:
    print('sanity test passes')
time.sleep(2)

# =============== Login  ================

# data
username = 'standard_user'
password = 'secret_sauce'

# selectors
username_selector = '#user-name'
password_selector = '#password'
login_selector = '#login-button'

username_txbx = driver.find_element(By.CSS_SELECTOR, username_selector)
username_txbx.send_keys(username)

password_txbx = driver.find_element(By.CSS_SELECTOR, password_selector)
password_txbx.send_keys(password)

login_btn = driver.find_element(By.CSS_SELECTOR, login_selector)
login_btn.click()

print('login success')

# ============= add items to the cart ==========

item1_selector = '#add-to-cart-sauce-labs-bike-light'
item2_selector = '#add-to-cart-sauce-labs-backpack'
quantity_selector = '#shopping_cart_container > a > span'

item1_btn = driver.find_element(By.CSS_SELECTOR, item1_selector)
item2_btn = driver.find_element(By.CSS_SELECTOR, item2_selector)

item1_btn.click()

time.sleep(1)

quantity_span = driver.find_element(By.CSS_SELECTOR, quantity_selector)

if int(quantity_span.text) == 1:
    print(f'items in the cart = ', quantity_span.text)

item2_btn.click()

if int(quantity_span.text) == 2:
    print(f'items in the cart = ', quantity_span.text)

time.sleep(5)

# ======== buy flow

cart_selector = '#shopping_cart_container > a'
checkout_selector = '#checkout'

driver.find_element(By.CSS_SELECTOR, cart_selector).click()  # once clicking

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, checkout_selector).click()

time.sleep(2)

details = ['#first-name', '#last-name', '#postal-code']
data = ['Gal', 'johanni', '198762']

for i in range(3):
    driver.find_element(By.CSS_SELECTOR, details[i]).send_keys(data[i])
    time.sleep(1)

time.sleep(4)

continue_selector = '#continue'
driver.find_element(By.CSS_SELECTOR, continue_selector).click()

time.sleep(2)

finish_selector = '#finish'
driver.find_element(By.CSS_SELECTOR, finish_selector).click()

final_title_selector = '#checkout_complete_container > h2'

if driver.find_element(By.CSS_SELECTOR, final_title_selector).text == 'Thank you for your order!':
    print('E2E test pass')
    driver.save_screenshot('final.jpg')
