vowels = "AEIOUaeiou"
name = input("Enter a word or sentence: ")
count = 0
for i in name.lower(): # lower it in passing an input in this program.
    for j in vowels:
        if i == j:
            count += 1  # or-else ( count = count +1 )
print(count)