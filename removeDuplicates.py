 # remove duplicates from array

nums = [0,0,1,1,1,2,2,3,3,4]


def removeDuplicates(nums):
    k = len(nums) # get length
    i = 0

    while i < k:
        look4 = nums[i]
        k = len(nums) # update length 
        if nums.count(look4) > 1:
            nums.remove(look4)
        else:
            i += 1

    k = len(nums) # update length
    return k

removeDuplicates(nums)
