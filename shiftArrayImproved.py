# Given an array, rotate the array to the right by k steps, where k is non-negative.


nums = [-1,-100,3,99]
#      [5,6,7,1,2,3,4]
#       0 1 2 3 4 5 6
k = 2

def rotateArray(nums, k): # nums == aray : k = how many times to shift
    if k == 0: # if array is to be shifted 0 times, return original array
        return nums
    i = 0 # counter
    length = len(nums) # get length of array
    while i < k : # while i is less than the number of times to shift
        num = nums[-1] # get element at the end of the array
        nums.pop(-1) # remove element at the end of the array
        nums.insert(0, num) # insert the element that was removed to the beginning of array
        i += 1
  
    return nums

nums = rotateArray(nums, k) # function call

length = len(nums)
for i in range(length):
    print (nums[i]) # print elements of newly arranged array in order from first to last

    
