print("This program checks if a number is kaprekar")
def get_valid_string():
    try:
      while True: 
       numString=input("Enter the number: ")
       if numString.isdigit() and int(numString)>0:
          return numString
       else:
          print("Invalid Input. Enter a Positive Integer")
    except KeyboardInterrupt:
       print("\nInput Interrupted. Exiting...")
       return None


def karpekarForm(x):
    if x=="1":
        return "1 is a Kaprekar Number"
    elif x=="9":
        return "9 is a Kaprekar Number as its square is 81 and 8+1=9"
    if len(x)>1:
     strx=str(int(x)**2)
     for i in range(1,len(strx)):
        if int(strx[:i])+int(strx[i:])==int(x):
            return f"{x} is a Kaprekar Number as its square is {strx} and {strx[:i]}+{strx[i:]}={x}"
   
    return f"{x} is not a Kaprekar Number"

numString=get_valid_string()
if numString!=None:
   res=karpekarForm(numString)
   print(res)

   

