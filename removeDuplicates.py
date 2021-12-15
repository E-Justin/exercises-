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
            if j == k:
                break
        if j < k and nums[i] != nums[j]:
            j += 1
        if j == k:
            i += 1
            j = i + 1
        k = len(nums)

    

    
    k = len(nums)

    for i in range(k):
        print(nums[i])

    print (k)
    
    return k



