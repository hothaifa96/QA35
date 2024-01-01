import requests
import pytest

# data = [{'name': 'hodi'},
#         {'name': 'hodi'},
#         {'name': 'maor'},
#         {'name': 'hodi'}]  # we have a list of dict
#
# print(len(data))  # the number of dict in the list
# c = 0  # temp variables named c to count the hodis objects
# for obj in data:  # for each dict in the list of dict's
#     if obj['name'] == 'hodi':  # if the value of the key 'name' is 'hodi'
#         c = c + 1  # add 1 to the counter
# print(f'we have {c} hodi"s')  # pretty printing

def test_1():
    url = 'https://www.fruityvice.com/api/fruit/all'
    res = requests.get(url)  # http response for the get request

    data = res.json()  # get the content of the response which is list of dicts

    print(type(data))  # the data type is list
    print(data)  # list of dict's   => [{},{},{},......,{}]
    print(type(data[0]))  # the type is dict
    #  data[0]  V
    #  data = [{ },{ },{ },......,{ }]

    for fruit in data: # for each dict named fruit in [{},{}]
        if fruit['name'] == 'Blackberry': # if the name of the fruit
            actual = fruit['family']
    expected = 'Rosaceae'
    assert actual == expected
