sum_of_numbers = 0
count = int(input("Enter a number that you want to Sum it! "))
for a in range(1, count):
    sum_of_numbers += a # or else we have to write like a (sum_of_numbers = sum_of_numbers + a)
print(sum_of_numbers)

# without using the loop concept is:
# num = int(input("Enter any number: ")
# print(num*(num+1))//2)