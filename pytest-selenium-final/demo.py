from selenium import webdriver
from selenium.webdriver.common.by import By


def mid_night_balance():
    url = 'https://demo.applitools.com/'
    selectors = ['#username', '#password', '#log-in']
    balance_selectors = [
        'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)',
        'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div:nth-child(3) > div.balance-value.danger',
        'body > div > div.layout-w > div.content-w > div > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(1) > td.text-right.bolder.nowrap > span'
    ]
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.CSS_SELECTOR, selectors[0]).send_keys('hodi')
    driver.find_element(By.CSS_SELECTOR, selectors[1]).send_keys('12345')
    driver.find_element(By.CSS_SELECTOR, selectors[2]).click()

    balance = driver.find_element(By.CSS_SELECTOR, balance_selectors[0]).text
    due = driver.find_element(By.CSS_SELECTOR, balance_selectors[1]).text
    amount = driver.find_element(By.CSS_SELECTOR, balance_selectors[2]).text

    print(f'balance = {balance} {type(balance)}')
    balance = int(balance[1:])

    print(f'due = {due} {type(due)}')
    due = int(due[1:])

    print(f'amount = {amount} {type(amount)}')
    amount = int(amount.replace(' ', '').replace(',', '')[:-3])

    actual = balance + amount - due
    return actual

url = 'https://demo.applitools.com/'
selectors = ['#username', '#password', '#log-in']
balance_selectors = [
    'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)',
    'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div:nth-child(3) > div.balance-value.danger',
    'body > div > div.layout-w > div.content-w > div > div > div:nth-child(2) > div > div > table > tbody > tr:nth-child(1) > td.text-right.bolder.nowrap > span'
]
driver = webdriver.Chrome()
driver.get(url)
driver.find_element(By.CSS_SELECTOR, selectors[0]).send_keys('hodi')
driver.find_element(By.CSS_SELECTOR, selectors[1]).send_keys('12345')
driver.find_element(By.CSS_SELECTOR, selectors[2]).click()

table = driver.find_elements(By.CLASS_NAME,'bolder')
print(table)
sum = 0
for rows in table:
    amount = float(rows.text[:-4].replace(',','').replace(' ',''))
    sum += amount

print(sum)