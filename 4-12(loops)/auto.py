import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()         # browser window
driver = webdriver.Chrome()  # browser window
# driver = webdriver.Edge()         # browser window

driver.get('https://google.com')  # open this site
time.sleep(3)  # wait 3 seconds
driver.get('https://www.tesla.com/')
time.sleep(3)  # wait 3 seconds

order_btn = driver.find_element(By.CSS_SELECTOR, '#block-tesla-frontend-content > div > section > div > div > div.tcl-homepage-hero__buttons.tcl-homepage-hero__buttons-on-desktop > section > a.tds-btn.tcl-button.tds-btn--tertiary.tcl-button--tertiary')

order_btn.click()

time.sleep(3)
