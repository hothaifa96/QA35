# def hello():
#     print('red RAT hand !')
#
#
# # l1 = [1,44,5,1]
# #
# # print(l1.sort()) # -> None
# # print(l1)
#
# hello()


# def odd_sum(nums):
#     s = 0
#     for n in nums:
#         if n % 2 == 1:
#             s = s + n
#     return s
#
#
# numbers = [9, 7, 2, 4, 1]
# numbers2 = [55, 2, 1, 4, 2]
# # s = sum(numbers)
# # print(s)
#
#
# # cap - water - AC -> coffee
# # AC -> None
# # odd_sum(numbers)
# # odd_sum(numbers2)
# # odd_sum([9, 8, 7, 6, 5, 4, 3, 2, 1])
#
# sum_of_numbers = odd_sum(numbers)
# length = len(numbers)
#
# print(sum_of_numbers//3)

# in my building there are 2 elevators lets call them the left and the right
# the algorithm  works like this
# the nearest elevator will come to you but if the distance is equal the
# right one will come
# write a python code that take the call floor number and the position of the
# two elevators and return the name of the elevator on the way


def get_elevator(right, left, call):
    d_right = abs(right - call)  # 3
    d_left = abs(left - call)  # 5

    if d_right <= d_left:
        return 'right'
    else:
        return 'left'


sit1 = get_elevator(3, 1, 0)
sit2 = get_elevator(0, 0, 8)
sit3 = get_elevator(4, 5, 2)

print(sit3, sit2, sit1)

for i in range(10):
    print('hello')

print(sit1)

# to run python code from the terminal use :
# mac linux -> ' python3 filename.py '
# windows -> ' python filename.py '