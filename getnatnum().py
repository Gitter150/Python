def getnatnum():
    while True:
        try:
            n = int(input("Enter the number: "))
            if n>0:
                return n
            else:
                print("Invalid Input. Enter a positive number. ")
        except ValueError:
            print("Invalid Input. Only Enter Natural Numbers, not Letters or Decimal Numbers.")

