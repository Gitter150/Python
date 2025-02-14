from math import sqrt
n=10000
k=1/2
reciprocal_list=[(1/x)**k for x in range(1,n+1)]
print(f"Sum = {sum(reciprocal_list)}")