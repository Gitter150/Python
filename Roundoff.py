def roundoff(x):
    if x-int(x)>=0.5:
        x=int(x)+1
        return(x)
    else: return int(x)
n=float(input("Enter the number to be rounded off: "))
print(f"{n} is rounded off to {roundoff(n)}")

    