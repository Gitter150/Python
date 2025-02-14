import random 
nums=[str(x) for x in range(1,10)]
alpha1=list("abcdefghijklmnopqrstuvwxyz")
alpha2=[x.upper() for x in alpha1]
alnum=alpha1+alpha2+nums
print("Welcome to the Password Generator!")


def getnatnum():
    while True:
        try:
            n = int(input("Enter the length of the required password: "))
            if n>0:
                return n
            else:
                print("Only enter a positive integer! (Greater than zero)") 
            
        except ValueError:
            print("Enter only a positive integer!")
        except KeyboardInterrupt:
            print("Keyboard Interrupted. Exiting...")

print("Do you want any special characters in your password? (!,@,#,$,%,&)")


while True:
    cho=input("Yes or No?: ").lower()
    if cho=="yes" or cho=="no":
         break
    else: 
         print('Enter either "yes" or "no"')
    
   

if cho=="yes":
    alnum=alnum+['!','@','#','$','%','&']



length=getnatnum()
        
passlist=random.choices(alnum,k=length)
print("Your Password is: ",''.join(passlist))


