# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

nums = [2,2,1,5,1]


def singleNumber(nums):
    singleNum = None
    length = len(nums) # get length
    i = 0
    while i < length: # while i is in range
        if nums.count(nums[i]) == 1: # if the number is only found once
            singleNum = nums[i] # assign single value to variable
            break #leave loop
        i += 1
    return singleNum # return single value

   
print(singleNumber(nums))

