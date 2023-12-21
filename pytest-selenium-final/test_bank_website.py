import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from demo import *

class TestStringFunctions:
    def test_len(self):
        word = 'hodi'
        actual = len(word)
        expected = 33
        assert actual == expected

    def test_replace_function(self):
        # data
        word = 'pizza'
        actual = word.replace('z', 'e')
        expected = 'pieea'
        assert actual == expected


class TestLogIn:
    def test_sanity(self):
        url = 'https://demo.applitools.com/'
        driver = webdriver.Chrome()
        driver.get(url)
        expected = 'ACME Demo App by Applitools'
        actual = driver.title

        assert actual == expected

    def test_login(self):
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
        expected_username = 'Jack gomez'

        assert actual_url == expected_url and expected_username == actual_username


class TestSystem:
    def test_check_balance(self):
        expected = 350
        url = 'https://demo.applitools.com/'
        selectors = ['#username', '#password', '#log-in']
        driver = webdriver.Chrome()
        driver.get(url)
        driver.find_element(By.CSS_SELECTOR, selectors[0]).send_keys('hodi')
        driver.find_element(By.CSS_SELECTOR, selectors[1]).send_keys('12345')
        driver.find_element(By.CSS_SELECTOR, selectors[2]).click()
        balance = driver.find_element(By.CSS_SELECTOR,'body > div > div.layout-w > div.content-w > div > div > div.element-wrapper.compact.pt-4 > div.element-box-tp > div > div > div > div.balance.hidden-mobile > div.balance-value > span:nth-child(1)').text
        actual = int(balance[1:])

        assert actual == expected

    def test_balance_mid_noght(self):
        expected = 1420
        actual = mid_night_balance()

        assert actual == expected

