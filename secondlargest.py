string = input().strip()
nums = string.replace(","," ").split()
nums = [int(x) for x in nums]
nums.sort()
nums.remove(nums[-1])
print(nums[-1])
