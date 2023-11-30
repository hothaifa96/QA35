# employees_salary = [18000, 20000, 10000, 11000, 7659, 8950]
#
# # print the salary after taxis about 36%
# # list -> []
#
# for s in employees_salary:
#     print(f'the final salary = {s*0.64}')
#
# # employees_salary[0] * 0.64
# # employees_salary[1] * 0.64
# # employees_salary[2] * 0.64

names = ['noa', 'itay', 'noor', 'yohanatan', 'hodi', 'tanya', 'dana']
# name= ' '.join(names)
# print(name)
# for n in names[: len(names)//2]:
# for n in names[: len(names) // 3]:  # third
#     print(n.upper())

# for n in names:
#     if n[1] == 'a':
#         print(n)
short_names = []

for n in names:
    if len(n) <= 4:
        short_names.append(n)

print(short_names)
print(names)
