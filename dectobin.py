def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary += str(remainder) 
        decimal = decimal // 2
    
    return binary[::-1]

# Example usage
while True:
  try:
     decimal_number = int(input("Enter a decimal number: "))
     if decimal_number>=0 or decimal_number<0:
         break
  except ValueError:
      print("Invalid Input. Enter a decimal integer. ")
      



binary_representation = decimal_to_binary(decimal_number)
print(f"{decimal_number} in binary is: {binary_representation}")
