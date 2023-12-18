import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
username = 'standard_user'
password = 'secret_sauce'
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
swag_label = driver.find_element(By.CSS_SELECTOR, '#root > div > div.login_logo')
username_input = driver.find_element(By.CSS_SELECTOR, '#user-name')
username_input.send_keys(username)
time.sleep(1)
password_input = driver.find_element(By.CSS_SELECTOR, '#password')
password_input.send_keys(password)
time.sleep(1)
login_btn = driver.find_element(By.CSS_SELECTOR, '#login-button')
login_btn.click()
time.sleep(1)
add_to_cart = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
add_to_cart.click()
time.sleep(1)
add_to_cart2 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
add_to_cart2.click()
time.sleep(1)
Your_Cart = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a > span')
Your_Cart.click()
time.sleep(1)
checkout = driver.find_element(By.CSS_SELECTOR, '#checkout')
checkout.click()
time.sleep(1)
first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
first_name.send_keys('hamad')
time.sleep(1)
last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
last_name.send_keys('shahen')
time.sleep(1)

zip = driver.find_element(By.CSS_SELECTOR, '#postal-code')
zip.send_keys(1234)
time.sleep(1)
next = driver.find_element(By.CSS_SELECTOR, '#continue')
next.click()
time.sleep(1)
finish = driver.find_element(By.CSS_SELECTOR, '#finish')
finish.click()
time.sleep(1)

if driver.current_url == 'https://www.saucedemo.com/checkout-complete.html':
    print('login test pass')
else:

    print('login test fail')
driver.close()

# ================ the challenge ===================

import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

user_name = driver.find_element(By.CSS_SELECTOR, '#user-name')
user_name.send_keys('problem_user')
time.sleep(1)
password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('secret_sauce')
time.sleep(1)
login = driver.find_element(By.CSS_SELECTOR, '#login-button')
login.click()
time.sleep(1)
add_to_cart = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
add_to_cart.click()
time.sleep(1)
remove = driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
remove.click()
if driver.current_url == 'add-to-cart-sauce-labs-backpack/':
    print('go')
else:
    print('bug remove')
time.sleep(1)

add_to_cart1 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
add_to_cart1.click()
if driver.current_url == '#remove-sauce-labs-backpack':
    print('go')
else:
    print('bug add')
time.sleep(1)
in_add_to_cart = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-fleece-jacket')
in_add_to_cart.click()
time.sleep(1)
next = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')
next.click()
time.sleep(1)
checkout = driver.find_element(By.CSS_SELECTOR, '#checkout')
checkout.click()
time.sleep(1)
first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
first_name.send_keys('hamad')
time.sleep(1)
last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
last_name.send_keys('shahen')
time.sleep(1)
zip = driver.find_element(By.CSS_SELECTOR, '#postal-code')
zip.send_keys(1234)
time.sleep(1)
continu = driver.find_element(By.CSS_SELECTOR, '#continue')
continu.click()
time.sleep(1)
cancel = driver.find_element(By.CSS_SELECTOR, '#cancel')
cancel.click()
time.sleep(1)
continue_shoping = driver.find_element(By.CSS_SELECTOR, '#continue-shopping')
continue_shoping.click()
time.sleep(1)
sauce_labs_backpack = driver.find_element(By.CSS_SELECTOR, '#item_4_title_link > div')
sauce_labs_backpack.click()
time.sleep(1)
add_to_cart2 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-fleece-jacket')
add_to_cart2.click()
if driver.current_url == '#remove-Sauce-Labs-Fleece-Jacket':
    print('go')
else:
    print('bug 2 add')

time.sleep(1)
back = driver.find_element(By.CSS_SELECTOR, '#back-to-products')
back.click()
time.sleep(1)
select_class = driver.find_element(By.CSS_SELECTOR,
                                   '#header_container > div.header_secondary_container > div > span > select')
select_class.click()
time.sleep(1)
a_z = driver.find_element(By.CSS_SELECTOR,
                          '#header_container > div.header_secondary_container > div > span > select > option:nth-child(1)')
a_z.click()
if driver.current_url == '#header_container > div.header_secondary_container > div > span > select > option:nth-child(2)':
    print('go')
else:
    print('bug a_z')

time.sleep(1)
img = driver.find_element(By.CSS_SELECTOR, '#item_4_img_link > img')
img.click()
if driver.current_url == '#inventory_item_container > div > div > div.inventory_details_img_container > img':
    print('go')
else:
    print('bug img')
time.sleep(1)
driver.close()
