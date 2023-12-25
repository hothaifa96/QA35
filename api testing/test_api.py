import pytest
import requests


class TestSanity:
    def test_google(self):
        url = 'https://google.com'
        res = requests.get(url)
        actual = res.status_code
        expected = range(200, 300)  # [200,2001......299]
        # assert 200 <= actual < 300
        assert actual in expected

    def test_amazon_n(self):
        url = 'https://amazon.com'
        res = requests.get(url)
        actual = res.status_code
        expected = range(200, 300)
        assert actual not in expected


class TestIntegration:
    def test_int1(self):
        url = 'https://jsonplaceholder.typicode.com/users'
        res = requests.get(url)
        expected = 'leanne'
        actual = res.text.lower()
        assert expected in actual

    def test_valid_json(self):
        #  { }
        url = 'https://jsonplaceholder.typicode.com/users'
        res = requests.get(url)
        number_of_open = res.text.count('{')
        number_of_closed = res.text.count('}')
        assert number_of_closed == number_of_open

    def test_definition(self):
        # write a code to check show the
        # appearances of the definition word
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/apple'
        res = requests.get(url)
        actual = res.text.count('definition')
        expected = 14
        assert actual == expected


