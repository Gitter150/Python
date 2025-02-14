import time
print("This is a Timer! Enter the time for countdown in the specified format:")

def hour():
    while True:
        try:
            n = int(input("Enter the Hours:\n (0 to 23)--> "))
            if n>=0 and n<24:
                return n
            else:
                print("Invalid Input. Enter in the range of 0 Hours to 23 Hours")
        except ValueError:
            print("Invalid Input. Enter only an integer for Hours.")

def minute():
    while True:
        try:
            n = int(input("Enter the Minutes:\n (0 to 59)--> "))
            if n>=0 and n<60:
                return n
            else:
                print("Invalid Input. Enter in the range of 0 Minutes to 59 Minutes")
        except ValueError:
            print("Invalid Input. Enter only an integer for Minutes")

def second():
    while True:
        try:
            n = int(input("Enter the Seconds:\n (0 to 59)--> "))
            if n>=0 and n<60:
                return n
            else:
                print("Invalid Input. Enter in the range of 0 Seconds to 59 Seconds")
        except ValueError:
            print("Invalid Input. Enter only an integer for Seconds")

hours=hour()
minutes=minute()
seconds=second()

total_time=hours*3600+minutes*60+seconds

print("Your Timer starts in")

for i in range(3,0,-1):
    print(i)
    time.sleep(1)
print("START!")
time.sleep(1)
for i in range(total_time, -1, -1):
    print(i)
    time.sleep(1)

print("FINISHED!")