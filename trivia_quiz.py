from requests import get
from html import unescape
from os import system
from time import sleep

print("Welcome to the trivia question generator!")

while True:
    print("Here is your question:")
    try:
        response = get("https://opentdb.com/api.php?amount=1").json()["results"][0] #interacting with the api endpoint 
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
        sleep(3)
        system("cls")
    else:
        print("Oops, that's the wrong answer.")
        print("The correct answer is: "+correct_answer)
        sleep(4)
        system("cls")

    if input("Want another question? Yes or No: ").strip().lower() != "yes":
        print("Alright! Thank you for playing.\nExiting...")
        sleep(3)
        system("cls")
        break
    



