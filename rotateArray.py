# Given an array, rotate the array to the right by k steps, where k is non-negative.

nums = [1,2,3,4,5,6,7]
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Output: [5,6,7,1,2,3,4]
k = 3


def rotateArrayToRight(times, arr):
    for i in range(times):
        toMove = arr[-1]
        arr.pop(-1)
        arr.insert(0, toMove)
    return arr


rotateArrayToRight(k, nums)

   
