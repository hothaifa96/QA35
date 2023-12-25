# # pip3 install requests >=> to download requests lib
#
# import requests
#
# # send http request to url
# # response will be fetched
#
# url = 'https://google.com/'
# res = requests.get(url)
#
# # print(res)  # response [status code]
# # print(res.text)  # the content of the website HTML/ image text
# # print(res.text.count('input'))  # number of inputs in google home page
# # print(res.text.count('div') // 2)  # number of inputs in google home page
# print(res.url)  # the url of the website
# print(res.status_code)
# status = res.status_code
# # 201 // 100 = 2
# # if status // 100 ==2:
# #     print('success')
# # else:
# #     print('failed')
# if 200 <= status < 300:
#     print('success')
# else:
#     print('failed')



# write a code to check show the
# appearances of the definition word
