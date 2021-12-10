# Given an integer array nums, move all 0's to the end of it while 
# maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

def moveZeroes(nums):
    index = 0
    length = len(nums)

    while index < length:
        if nums[index] == 0:
            zero = nums[index]
            nums.remove(zero) # removes zero if found
            nums.append(zero) # appends the zero to the back of the array
        index += 1
    return nums

nums = moveZeroes(nums)

length = len(nums)
index = 0
while index < length:
    print (nums[index]) # prints elements of array one at a time
    index += 1
