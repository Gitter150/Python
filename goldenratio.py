print("This program calculates the golden ratio upto a specific accuracy!")

def getnatnum():
    while True:
        try:
            n = int(input("Enter the parameter of accuracy: "))
            if n > 0:
                return n
            else:
                print("Enter only a natural number (greater than 0).")
        except ValueError:
            print("Enter only a natural number (an integer).")


par = getnatnum()
fib=[0]*par

try:
  fib[0]=0
  fib[1]=1
  for i in range(2,par):
    fib[i]=fib[i-1]+fib[i-2]
  
  print(f"The Golden Ratio is: {fib[par-1]/fib[par-2]}")
except:
   print(f"The Golden Ratio is: Undefined")
a="th"
match par:
   case 2:
      a="nd"
   case 1:
      a="st"
   case 3:
      a="rd"
   
print(f"..so the way this actually works is that i first find the {str(par)+a} fibonnaci number and then divide it by the previous number.\n The reason this works is because as the fibonnaci series approaches infinity,\nthe ratio of two successive terms approaches golden ratio.")
