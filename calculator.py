prompt = input("What Can I Do For You?\n")
match prompt.lower():
    case "hi":
        print("Hi!")
    case "hello":
        print("Hello!")
    case "Who are you?":
        print("Iam a Python AI Chat Bot!")