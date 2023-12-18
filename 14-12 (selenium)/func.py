# import math
#
#
# def greet():
#     print('hello')
#
#
# # x = 4
# def greet_with_name(name):
#     print(f'hello {name}')
#     # print(x)
#
#
# # print(name)
# # greet()
# # print('im a superman')
# # greet_with_name('oshri')
# # greet_with_name('ben')
# # greet_with_name('yoni')
#
# def greet_name_age(name, age):
#     print(f'my name is {name} and im {age} y.o')
#     return 3
#
#
# x = greet_name_age('hodi', 14)
#
# l = len('sss')
#
# # Epic                      Project
#     # feature               file
#         # userSotry         class
#            #TEST            function


# def divide(x, y):
#     return x // y
#
#
# ans = divide(5, 9)
#
# print(ans)

from selenium import webdriver


def get_Driver():
    driver = webdriver.Chrome()
    return driver


def sanity_test():
    driver = get_Driver()
    driver.get('https://google.com')
    print(driver.current_url)
    return driver.current_url
def login():
    driver = get_Driver()
    sanity_test()



if sanity_test() == 'https://www.google.com/':
    print(True)
