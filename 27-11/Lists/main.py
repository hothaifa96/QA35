# write a code to print the 5 students grades and the avg

# st1_grade = 99
# st2_grade = 11
# st3_grade = 98
# st4_grade = 71
# st5_grade = 92
#
# print(f'the grade of the first student is {st1_grade}')
# print(f'the grade of the second student is {st2_grade}')
# print(f'the grade of the third student is {st3_grade}')
# print(f'the grade of the fourth student is {st4_grade}')
# print(f'the grade of the fifth student is {st5_grade}')
#
# print(f'the average is {(st1_grade + st2_grade + st3_grade + st4_grade + st5_grade) / 5}')


# grades = [92, 99, 66, 11]
#
# print(grades)
# print(grades[2])
# print(grades[-1])
# print(grades[:2])


# foods = ['pizza', 'pasta', 'hamburger', 'chips', 'ice cream']
# numbers = [22, 4151, 561, 61, 6, 16, 1, -612, 71, 1, 6, 1, 61, 6, 11, -92]
# print(len(foods))  # return the many how many items in list
# print(foods[-2][:3:-1])  # nested slicing
#
# if 'hummus' in foods:  # check if item exist
#     print('i want hummus')
# else:
#     print(f'i want {foods[2]}')

# print(foods)
# foods[1] = 'ravioli'  # change item value
# print(foods)
#
# foods.append('shakshoka')  # append item
# print(foods)
#
# foods.insert(1, 'shawarma')  # insert by index
# print(foods)
#
# foods.pop(0)  # delete by the index
# print(foods)
#
# if 'chips' in foods:
#     foods.remove('chips')  # remove by the value
# print(foods)

# foods.sort(reverse=True)  # DESC Z-A
# # foods.sort() # ASC A-Z
# print(foods)

# numbers.sort()
# print(numbers[::-1])   #
# numbers.reverse()
# print(numbers)


# numbers.clear()
# print(numbers)

# print(numbers)  # count the item
#
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))


# list1 = [1, 2, 44, 'hello', 55]
#
# # Write a program to count the number of items stored in a list.
# # print(f'the list length is {len(list1)}')
#
# # write a program to reverse the list order in python
#
# # list1.reverse()
# # print(list1)
#
# # write a python code to delete the word hello from the list if its exists
# # if 'hello' in list1 :
# #     list1.remove('hello')
# #
# # print(list1)
# # # delete the last item from the list1
# list1.pop()


# list2 = []
#
# # given list2
# # 1 write a python code to print the datatype of list2
# # <class list>
# # print(type(list2))
#
# # 2 add 2 values from the user input as string
# list2.append(input('please enter a word : '))  # short
# x = input('please enter a word : ')
# list2.append(x)
# print(list2)
#
# # 3 ask the user for another name  if the name ends with 'r' or the length
# # of it greater than 4 add it to the list and print the list at the end
# # תבקשו מהמשתמש עוד שם במידה והשם נגמר באות ר או שאורכו של השם גדול
# # ממש מ 4 תוסיפו את השם לרשימה והדפיסו את הרשימה
#
# x = input('enter another word : ')
# if x.endswith('r') or len(x) > 4:
#     list2.append(x)
#
# # if x[-1] == 'r':
# #     list2.append(x)
# # elif len(x) > 4:
# #     list2.append(x)
# print(list2)
#
# fullname = '<><>'.join(list2)
# print(fullname)
# print(list2)


# name = ['ruth', 'guedalia','mohse' ,'zeno']
#
# fullname = ' '.join(name) # concate all the items of the list to one string and separate them using the ''
# print(fullname)


food = 'mama maglione pizza'
food_list = food.split()  # split str -> list
print(food_list)
food_list[0], food_list[1] = food_list[1], food_list[0].upper()  # swap the value and mama in uppercase
food = ' '.join(food_list)  # new str form the lists    list -> str
print(food)
