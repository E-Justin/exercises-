# program to remove duplicate values.

nums = [1,1]
#       0 1 2 3 4 5 6 7 8 9
def removeDuplicates(nums):
    k = len(nums) # to hold the number of elements in the array = 10
   
    i = 0
    j = i + 1
    while i < k and j < k:
        while nums[i] == nums[j]: # if both elements have the same value.
            nums.pop(i) # removes element from index i
            k = len(nums)
            if j == k: # if j has reached past available index
                break
        if j < k and nums[i] != nums[j]: # while j is within range and the two values are not the same
            j += 1
        if j == k: # if j has reached past available index
            i += 1 # increment i by one
            j = i + 1 # set j to the position after i
        k = len(nums)

    

    
    k = len(nums)

    for i in range(k):
        print(nums[i])

    print (k)
    
    return k





    
    
