import sys
sys.set_int_max_str_digits(1000000)
def getnatnum():
    while True:
        try:
            n = int(input("Enter the number: "))
            if n>0:
                return n
            else:
                print("Invalid Input. Enter a positive number. ")
        except ValueError:
            print("Invalid Input. Only Enter Natural Numbers.")
print("This Is A Factorial Calculator.")
n=getnatnum()
fact=1
for i in range(n):
    fact*=(i+1)
print(f"{n}! = {fact}")
print(f"No. Of Digits = {len(str(fact))}")
