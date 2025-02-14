from math import comb

n = int(input("This program prints the pascal's triangle!\nEnter the number of rows: "))

if n%2 == 0:
    for k in range(n+1):
        for i in range(0,n//2 + 1):
            for j in range(0,i+1):
                print(f"{comb(k, j)} ",end = "")
            print('')
