from math import sqrt, floor

def isprime(x):
    sqrtnum = floor(sqrt(x))
    if x == 2 or x == 3 or x == 5 or x ==7:
        return True
    if x%2 == 0 or x%3 == 0 or x%5 == 0 or x%7 == 0 :
        return False
    for i in range(1,sqrtnum+1,2):
        if i==1:
            continue
        if x%i == 0:
            return False
    return True


     
print(isprime(127))
  






    