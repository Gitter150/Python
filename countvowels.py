print("This program counts the number of vowels in a given string!")
s = input("Enter the string: ")
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
count = 0

for x in s:
    if x in vowels:
        count += 1

print(f'In "{s}", there are {count} vowels')



