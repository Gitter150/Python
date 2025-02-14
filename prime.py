from math import sqrt
def is_prime(x):
    
    if x in {0,1}:
        return False
    if x in {2,3}:
        return True
    if x % 2==0 or x % 3==0:
        return False
    i = 5
    while i<=int(sqrt(x))+1:
        if x % i == 0:
            return False
        i += 2
    return True
sum = 1.0
count = 0

n = 10000000
for i in range(1,n+1,2):
    count += 1
    if is_prime(i):
        sum += 1/i if count % 2 == 0 else -1/i
    else:
        continue
print(4*sum)


    

        
    
