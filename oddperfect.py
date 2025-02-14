from math import sqrt
def is_perfect(x:int)->bool:
    count=0
    for i in range(1,int(sqrt(x))+2):
        if x%i==0:
            count=count+i+x//i
    return count==x
print(is_perfect(6))