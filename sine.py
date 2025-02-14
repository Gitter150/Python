from math import sin, cos, tan, radians, pi

from sympy import sympify, rad

def zero_if_small(value, threshold=1e-10):
    
    if abs(value) < threshold:
        return 0.0
    else:
        return value

print("Calculate the sine, cosine, and tangent of any angle!")

while True:
    choice = input('Enter "deg" for degree measure, "rad" for radian measure: ').strip()
    if choice == 'deg' or choice == 'rad':
        break
    else:
        print('Invalid choice. Enter either "deg" or "rad"')

if choice == 'rad':
    while True:
        try:
            angrad = input("Enter the angle in radians: ")
            angradsymp = sympify(angrad).evalf()
            break
        except (ValueError, TypeError):
            print("Invalid Input. Enter a valid mathematical expression")

    sin_val = sin(angradsymp)
    cos_val = cos(angradsymp)
    tan_val = sin_val / cos_val if cos_val != 0 else float('inf')

    print(f"Sin({angrad}) = {zero_if_small(sin_val)}")
    print(f"Cos({angrad}) = {zero_if_small(cos_val)}")
    print(f"Tan({angrad}) = {zero_if_small(tan_val)}" if angrad!=pi/2 else f"Tan({angrad}) = Undefined (cos({angrad}) is zero)")

if choice == 'deg':
    while True:
        try:
            angdeg = int(input("Enter the angle in degrees: "))
            angdegsymp = sympify(angdeg)
            angdegtorad = radians(angdegsymp)
            break
        except ValueError:
            print("Invalid Input. Enter a valid number.")

    sin_val = sin(angdegtorad)
    cos_val = cos(angdegtorad)
    tan_val = sin_val / cos_val if cos_val != 0 else float('inf')

    print(f"Sin({angdeg}) = {zero_if_small(sin_val)}")
    print(f"Cos({angdeg}) = {zero_if_small(cos_val)}")
    print(f"Tan({angdeg}) = {zero_if_small(tan_val)}" if angdeg != 90 else f"Tan({angdeg}) = Undefined (cos({angdeg}) is zero)")


 

      