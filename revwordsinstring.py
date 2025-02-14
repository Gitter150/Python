x = input("Enter the string: ")
words = [y[::-1] for y in x.split()]
print(" ".join(words))
