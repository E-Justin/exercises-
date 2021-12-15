# Given an integer array nums, return true if any 
# value appears at least twice in the array, and return false if every element is distinct.

nums = [1,1,1,3,3,4,3,2,4,2]

def duplicates(nums):
    length = len(nums) # get length
    nums.sort() # sort in ascending order

    i = 1
    duplicates = False # set duplicates to False

    while i < length and duplicates == False: 
        if nums[i] == nums[i -1]: # if duplicate is found
            duplicates = True
            break
        else:
            i += 1
        if i == length: # if i has reached outside the available index
            duplicates = False

    return duplicates

print(duplicates(nums))
   
    






