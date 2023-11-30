# 2
# list1 = [1, 2, 3, 4, 5]
# # st1 = 'hodi'
# #
# # for (var_name) in (str/list):
# #     # what to do
# #
# for x in list1:
#     print(list1)
# 3

# cars = ['audi','bmw','cupra','tesla']
#
# for c in cars:
#     print(c)

# list1 = [100, 8, 7, 5, 1]
#
# for n in list1[:len(list1) // 2]:  # first half list
#     print(n)

# 4

# words = ['hello', 'python', 'pen', 'hello world']
#
# for w in words:
#     if len(w) < 4:
#         break # stop the loops if we found a word shorter than 4 char
#     print(w.upper())

# 6

# name = 'Donald trump'
# # print(name[-5:])  # last 5 chars
# # print(name[: len(name) // 3])  # first third of the name
# # print(f'we found {name.count("a")} a in the name')  # number of a's in the name
# # print('b' in name)  # in name contain 'b'
# # if 'b' not in name:
# #     print(False)
# # else:
# #     print(True)
# name_list = name.split()  # split convert the str to list and by the spces
# print(name_list)  # ['Donald','trump']
# # a = 1
# # b = 2
# #
# # tmp = a
# # a = b
# # b = tmp
# #
# # a, b = b, a
# name_list = name_list[::-1]  # reverse the values
# print(name_list)
#
# name_list[0] = name_list[0].upper()  # convert the letters to upper in the last name
# print(name_list)
#
# firstname_length = len(name_list[1])
#
# name_list[1] = name_list[1][:firstname_length // 2] + name_list[1][(firstname_length // 2)+1:]
# print(name_list)
#
# name = ' '.join(name_list) # list -> str ' '
# print(name)
# ['donald','trump'] = 'donald trump'


# 7
#      012345678901
# sen = 'hello world!'
#
# print(sen.find('o'))
# print(sen.rfind('o'))
#
# print(sen[:sen.find('o')])  # from the start till the first o
# print(sen[sen.rfind('o'):])  # from the last o till the end

# 8

# sen = 'hello world!'
#
# print(sen.replace('o', '')) # change every o to null

# 9

nums = [8, 1000, -3, 2, 5]
small_nums = []
avg = sum(nums) // len(nums)  # 202
# sum = 0  # 8 # 1008 # 1005 # 1007 # 1012
# for num in nums:
#     print(f'num -> {num} , sum ->{sum}')
#     sum += num
#
# print(sum)
# print(sum(nums))
# print(max(nums))
# print(min(nums))
#
# max_number = nums[0]
# for n in nums:
#     if n > max_number:
#         max_number = n
# print(max_number)
# print(sum(nums) / len(nums))

# nums.pop(len(nums) // 2)  # delete the center item
# print(nums)
#
# nums.sort()  # 1->999
# print(nums)

# print(nums)
# print(nums)
# print(nums)
# print(nums)
# print(nums)
#
# print(nums*5)
#
# for n in nums:
#     print(nums)
#
# nums.pop(0) # to delete the first item
# print(nums)

for n in nums:
    if n < avg:
        small_nums.append(n)  # add the value

print(small_nums)
