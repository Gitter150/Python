from requests import get
from html import unescape
from os import system
import time
print("Welcome to the trivia question generator!")
while True:
    print("Here is your question:")
    """ while True:
        try:
            amount = int(input("Enter the number of questions which you need: "))
            if amount<=0:
                print("Invalid number of questions. Enter the number of questions which you need (greater than 0)")
            else:
                break
        except ValueError:
            print("Invalid Input. Enter a positive number for the number of questions.") """

    try:
        response = get("https://opentdb.com/api.php?amount=1").json()["results"][0]
    except:
        print("The trivia generator API is not available at the moment.\nPlease try later.")
        break
    question = response["question"]
    correct_answer = response["correct_answer"]
    difficulty = response["difficulty"]
    category = response["category"]
    print("Category: "+unescape(category))
    print("Difficulty: "+difficulty)
    print("Q: "+unescape(question))
    if input("Enter your answer: ").strip().lower() == correct_answer.lower():
        print("Correct answer!")
        time.sleep(3)
        system("cls")
    else:
        print("Oops, that's the wrong answer.")
        print("The correct answer is: "+correct_answer)
        time.sleep(4)
        system("cls")
    if input("Want another question? Yes or No: ").strip().lower() != "yes":
        print("Alright! Thank you for playing.\nExiting...")
        time.sleep(3)
        system("cls")
        break
    



