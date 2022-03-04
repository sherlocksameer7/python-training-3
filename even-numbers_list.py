emp_list = []
new_list = []
for i in range(1, 11):
    # if i % 2 == 0:
        emp_list.append(i)
print(emp_list)
# new list creation
for j in emp_list:
    if j % 2 == 0:
        new_list.append(j)
print(new_list)