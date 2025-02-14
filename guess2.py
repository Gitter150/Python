import random

def getnatnum():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a natural number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a natural number (an integer).")

def play_guessing_game():
    target_number = random.randint(1, 100)
    print("Welcome to the game of Guess The Number!")
    print("I have chosen a random number between 1 and 100. Your job is to guess the number.")

    while True:
        guess = getnatnum()
        difference = abs(target_number - guess)

        if guess == target_number:
            print(f"Congratulations! You guessed the correct number: {target_number}")
            break
        elif difference > 20:
            print("Too far!")
        elif difference > 10:
            print("Getting closer!")
        else:
            print("Very close!")

        if guess < target_number:
            print("Try a higher number.")
        else:
            print("Try a lower number.")
        
        print("You can try again!")

play_guessing_game()
