nums = [1,1,691,1,2,2,3,3,4,4]

xor = 0
for num in nums:
    xor = xor ^ num
print(f"The duplicate element is {xor}")

