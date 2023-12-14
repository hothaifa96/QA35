# foods = ['shawarma','hummus','pizza']
#
# for food in foods :
#     print(food.upper())

# word = 'milkshake'
#
# for lt in word:
#     print(lt)

# get from the user his best 3 dishes and print them in one list

# foods = []
#
# # x = input('please enter a food : ')
# # foods.append(x)
# #
# # x = input('please enter a food : ')
# # foods.append(x)
# #
# # x = input('please enter a food : ')
# # foods.append(x)
# #
# # x = input('please enter a food : ')
# # foods.append(x)
#
# # print(range(start,end,jump))
# # print(range(4)) # -> 0,1,2,3
#
# for i in range(3): # [0,1,2]
#     x = input('enter a food')  # get the str from the user
#     foods.append(x)  # add to the list
#
# print(foods)


# for i in range(20):  # [0,1,2,3,4,5,6,7,.....,18,19]
#     if i % 2 == 0:  # print all the even numbers
#         print(i)


# ask the user to enter his password 3 time
# 3 if the password is admin print hello otherwise print nah


for i in range(3):  # run the code 3 times
    password = input('enter a password')  # get the password from the user
    if password == 'admin':  # if the password valid
        print('hello')  # greet the user
        break  # exit the loop
    else:
        print('nah')  # print nah for invalid passwords
