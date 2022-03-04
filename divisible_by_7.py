# emp_list = []
# for i in range(2, 101):
#     if i % 7 == 0:
#         emp_list.append(i)
# print(emp_list)

emp_list = [i for i in range(2, 101) if i % 7 == 0]
print(emp_list)

