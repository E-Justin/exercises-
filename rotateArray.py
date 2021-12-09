# task: rotate array k times
nums = [1,2,3,4,5,6,7]
k = 3
count = 0
i = 0

print (" Printing elements in array")
while i < len(nums):
    print (nums[i])
    i += 1

while count < 3:
    first = nums[0]
    nums.remove(first)
    nums.append(first)
    count += 1

i = 0
print (" Printing elements in array")
while i < len(nums):
    print (nums[i])
    i += 1
