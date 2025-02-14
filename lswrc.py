from collections import Counter
print("Enter the string: ")
string=input()

def lswrc(x: str) -> str:
    # c=Counter(x)
    # if all(c[char]==1 for char in c):
    #     return x
    storeSet=set()
    storeString= ""
    for i in range(len(x)):
        if x[i] not in storeSet:
           storeSet.add(x[i])
           storeString+=x[i]
    return storeString

        












print(lswrc(string))

         