# need to remove duplicate values

nums = [12, 15, 9, 12, 13, 21, 15, 72, 12]

i = 0
j = 1
length = len(nums) # gets length of array

print (" Current length of array : %d " % length)
print ("Printing elements in the array nums....")
while i < length:
    print (nums[i]) # print elements in array one at a time
    i += 1
    
i = 0

while i < len(nums) and j < len(nums) :
    while nums[i] == nums[j]: # if duplicate value is found
        toDelete = nums[j]
        print (" Deleting %d " % toDelete)
        nums.remove(toDelete) # remove duplicate value (indexes of all values decrease by 1 when .remove() is used)
        j = 1
        i = 0
    if j == len(nums) - 1: # if j has reached the end of the array
        i += 1
        j = i + 1
    j += 1


i = 0
length = len(nums) # get new length
print (" New length of array : %d " % length)
print ("Printing elements in the array nums....")
while i < length:
    print (nums[i])# print elements in array one at a time
    i += 1
    
