# reverse a given array

nums = [1, 2, 3]
nums2 = ["J","u","s","t","i","n"]

def reverseArray(nums):
    length = len(nums) # get length
    front = 0 # start at first element in array
    back = -1 # start at last element in array
    half = length // 2 # find middle
    while front < half: # while front index is less than half of the length
        nums[front], nums[back] = nums[back], nums[front] # swap front and back index
        front += 1 # move toward the middle by one element
        back -= 1 # move toward the middle by one element
    return nums


nums = reverseArray(nums2) # function call
length = len(nums2) # get length
for i in range (length): # while i is in range
    print (nums2[i]) # print one element at a time from front to back
  



