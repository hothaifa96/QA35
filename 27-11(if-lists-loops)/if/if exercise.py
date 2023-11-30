# indent


# if 'h' in 'hodi':
#     print('true')
# print('false')
#
#
# salary = 19000
# print(f'the salary is : {salary}')

# 8
# a = int(input('please enter a number : '))
# b = int(input('please enter a number : '))
#
# if a > b :
#     print(f'the greater number is {a}')
# elif a ==b :
#     print(f'the two vars equals {a}=={b}')
# else:
#     print(f'the greater number is {b}')
#
# x = int(input('enter a number : '))
# y = int(input('enter a number : '))
# z = int(input('enter a number : '))
#
# print(max(x, y, z))
# print(min(x, y, z))
#
# # if y < x > z:  # x > y and x > z
# #     print(x)
# # elif y > z:
# #     print(y)
# # else:
# #     print(z)

# 10

formula = input('please enter your formula using " " fir separation')
# formula = '1 + 1 = 2'
number1 = int(formula[0])
number2 = int(formula[4])
ans = int(formula[-2:])


if number1 + number2 == ans:
    print(True)
else:
    print(f'{number1} + {number2} = {number1+number2}')
