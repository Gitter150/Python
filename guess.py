import random

r = random.randint(1, 100)
print("Welcome to this game of Guess The Number!")
print("I will now choose a random number between 1 and 100. Your job is to guess the number.")

def getnatnum():
    while True:
        try:
            n = int(input("Enter your Guess!: "))
            if 1 <= n <= 100:
                return n
            else:
                print("Enter only a natural number (between 1 and 100).")
        except ValueError:
            print("Enter only a natural number (an integer).")

def choise(count=1):
    choice = getnatnum()
    
    if choice == r:
        print(f"You guessed it right! I had chosen the number {r}!")
        print(f"Number of trials: {count}!")
    else:
        if r - choice > 20:
            print("Too low!")
        elif choice - r > 20:
            print("Too high!")
        elif choice - r < 20 and choice - r > 0:
            print("A bit high!")
        elif r - choice < 20 and r - choice > 0:
            print("A bit low!")
        
        print("However, you can try again!")
        choise(count + 1)

choise()

