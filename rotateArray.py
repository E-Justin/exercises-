# Given an array, rotate the array to the right by k steps, where k is non-negative.

nums = [1,2,3,4,5,6,7]
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Output: [5,6,7,1,2,3,4]
k = 3


def rotateArray(nums, k):
    i = 0 

    while i < k:
        toMove = nums[-1] # stores the value to move
        nums.pop() # removes last element from array
        nums.insert(0, toMove) # inserts the value that was removed to the front of the array
        i += 1

   
