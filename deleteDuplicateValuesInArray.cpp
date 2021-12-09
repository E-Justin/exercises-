# program to remove duplicate values from an array

nums = [12, 15, 9, 12, 13, 21, 15, 72, 12]

i = 0
j = 1
length = len(nums)

print (" Current length of array : %d " % length)
print ("Printing elements in the array nums....")
while i < length:
    print (nums[i])
    i += 1
    
i = 0

while i < len(nums) and j < len(nums) :
    while nums[i] == nums[j]:
        toDelete = nums[j]
        print (" Deleting %d " % toDelete)
        nums.remove(toDelete) # if elements are the same, remove one of them
        j = 1
        i = 0
    if j == len(nums) - 1:
        i += 1
        j = i + 1
    j += 1


i = 0
length = len(nums)
print (" New length of array : %d " % length)
print ("Printing elements in the array nums....")
while i < length:
    print (nums[i])
    i += 1
    
