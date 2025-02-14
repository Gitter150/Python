string=input("Enter the string: ")
listString=string.split(' ')
revList=[x[::-1] for x in listString]
revstring=' '.join(revList)
print(revstring)