# name = 'Barak Obama In The house Make Noise'

# print(name)
# print(name[0])  # -> B
# print(name[5])  # ->
# print(name[20])  # ->  Error
# print(name[-1])  # -> a
# print(name[:7])  # -> Barak o
# print(name[:-4])  # -> Barak o
# print(name[:8])
# print(name[:])
# print(name[::-1])  # -> amabo karaB
# print(name[::-2])  # -> aaokrB

# ----------- string methods ----------------
# print(len(name))  # length of the word
# print(name.upper())  # make all the letters upper case
# print(name.lower())  # make all the letters lower case
# print(name.title())  # make all the Pascal Case
# print(name.strip())  # delete all the spaces before and after the str
# print(name.lstrip())  # delete all the extra spaces on the left
# print(name.rstrip())  # delete all the extra spaces on the right;

# print(name)
# print(name.replace('a', 'z'))  # replace old to new char replace(old, new)

# ip = '44.55.166.255'
# print(ip.replace('.', '\n'))

# creditcard = '4580 0000 0000 1234'
# print('*' * ( len(creditcard) - 4), creditcard[-4:])

# print(name.split())

# print(name.index('a'))  # return the index of the str
# print(name.rindex('a'))  # return the index of the last str
# print(name.count('a'))  # count the str in another str

# print(name.endswith('se'))
# print(name.startswith('ba'))
# print(name.islower())
# print(name.isupper())
# print(name.istitle())
# print('z' in name)  # true if the name contain z
# print(name.istitle())

# first_name = 'or'
# age = 26
#
# # print('the name is', first_name, 'the age is', age)
# print(f'hi my name is {first_name} and my age is {age}')  # formatted string


# ask the user to enter his name and print all the letters
# in a even index

# 0 1 2 3 4 5 6 7
# h o t h a i f a

# htaf

n = input('enter your name : ')
print(n[1::2])
