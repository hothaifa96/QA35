from  selenium import  webdriver
from selenium.webdriver.common.by import By

url = 'https://demo.applitools.com/'
selectors = ['#username', '#password', '#log-in']
driver = webdriver.Chrome()
driver.get(url)
driver.find_element(By.CSS_SELECTOR, selectors[0]).send_keys('hodi')
driver.find_element(By.CSS_SELECTOR, selectors[1]).send_keys('12345')
driver.find_element(By.CSS_SELECTOR, selectors[2]).click()
actual_url = driver.current_url
expected_url ='https://demo.applitools.com/app.html'
actual_username = driver.find_element(By.CSS_SELECTOR,'body > div > div.layout-w > div.menu-w.color-scheme-light.color-style-transparent.menu-position-side.menu-side-left.menu-layout-compact.sub-menu-style-over.sub-menu-color-bright.selected-menu-color-light.menu-activated-on-hover.menu-has-selected-link > div > div > div.logged-user-info-w > div.logged-user-name').text
expected_username = 'Jack Gomez'

assert actual_url == expected_url and expected_username == actual_username