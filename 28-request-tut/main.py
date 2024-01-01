import requests

# url = 'http://18.234.238.115/movies'
#
# res = requests.get(url)
#
# sc = res.status_code
#
# if 400 > sc >= 200:
#     print('pass')
# else:
#     print('fail')
#
# data = res.json()
# #
# # print(data) # list of dict's
# # print(type(data[0])) # dict
# #
# # for movie in data: # data is list   movie -> dict
# #     print(movie['title'])
# #
# # print(data)
#
# for movie in data:
#     if movie['year'] == 2014:
#         print(movie)


url2= "https://jsonplaceholder.typicode.com/users"

res = requests.get(url2)

print(res.status_code)

data = res.json()

print(len(data))

print(data)
for user in data:
    # print(user['name'].split(' ')[0]) # how to get the first name
    print(user['name'])
    # print('street : '+user['address']['street'])


# print(data[0]['address']['street'])