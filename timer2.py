import time
import os

print("This is a Timer! Enter the time for countdown in the specified format:")

def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            n = int(input(prompt))
            if min_val <= n <= max_val:
                return n
            else:
                print(f"Invalid Input. Enter in the range of {min_val} to {max_val}")
        except ValueError:
            print("Invalid Input. Enter only an integer.")

def hour():
    return get_valid_input("Enter the Hours (0 to 23): ", 0, 23)

def minute():
    return get_valid_input("Enter the Minutes (0 to 59): ", 0, 59)

def second():
    return get_valid_input("Enter the Seconds (0 to 59): ", 0, 59)

def format_time(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

hours = hour()
minutes = minute()
seconds = second()

total_time = hours * 3600 + minutes * 60 + seconds

print("Your Timer starts in")

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print("START!")
time.sleep(1)

while total_time > 0:
    os.system('cls')  # Clear the screen
    print(format_time(total_time))
    time.sleep(1)
    total_time -= 1

print("FINISHED!")
