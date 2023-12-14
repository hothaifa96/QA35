import time

from selenium import webdriver

print('hello')
# open the browser
driver = webdriver.Chrome()

# set the window size width , height
# driver.set_window_size(200,800)

# full display window
# driver.maximize_window()
# time.sleep(2)
# driver.minimize_window()


# go to google website
driver.get('https://google.com')

# returns the current url of the browser
print(driver.current_url)

# wait for 3 sec
time.sleep(3)

driver.get('https://ebay.com')
# driver.maximize_window()

# returns the current url of the browser
print(driver.current_url)
print(driver.title)
# if the driver load ebay site and another website opened the selenium will take a screen shot
if driver.current_url != 'https://ebay.com/':
    # takes a screenshot of the hole page
    driver.save_screenshot('./screen.jpg')

time.sleep(3)

# close the browser window
driver.close()

# search for mama maglionee pizza
