print("This calculator gives the sum of digits of a number!")
def getnatnum():
    while True:
        try:
            n = int(input("Enter the number: "))
            if n>0:
                return n
            else:
                print("Enter only a natural number")
        except ValueError:
            print("Enter only a natural number (an integer).")
num=getnatnum()

print(f"The sum of the digits of {num} is: {sum(int(x) for x in str(num))}")

