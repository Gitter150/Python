time = lambda x: f"{x//3600}:{(x%3600)//60}:{x%60}"
print(f"The time is\n{time(int(input("Enter the seconds: ")))}")