from itertools import permutations

def circular_permutations(x:list)->list:

    first=x[0]
    rest=x[1:]
    result=[]
    arrangements=permutations(rest)
    for arrangement in arrangements:
        circular_perm=(first,)+arrangement
        result.append(circular_perm)
    return result

list=['A','B','C','D']
for x in circular_permutations(list)[:-1]:
    print(x,end=(", " ))
print(circular_permutations(list)[-1])





