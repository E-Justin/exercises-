# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



def findDuplicates(nums):
    nums = sorted(nums) # sort array

    length = len(nums) # get length

    i = 1
    j = 0
    duplicateFound = False

    while i < length: # while i is less than the length
        if nums[i] == nums[j]: # if a duplcate is found
            duplicateFound = True # set to True
            break # exit loop
        else:
            i += 1 # increment index variables
            j += 1
    return duplicateFound

# Runtime: 614 ms
# Memory Usage: 22.5 MB
