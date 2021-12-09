# task: rotate array k times
nums = [-1,-100,3,99]
k = 2
count = 0
i = 0
length = len(nums)

print (" Printing elements in array")
while i < len(nums):
    print (nums[i])
    i += 1

def rotate(nums, k):
    count = 0
    while count < k:
        last = nums[length - 1] #store value of last element in the array
        # nums.remove(last) # remove the last element in the array (this one does not work with duplicate values)
        nums.pop() # removes last item from the array
        nums.insert(0 , last) # insert the removed value to the front of the array
        count += 1

rotate(nums, k)

i = 0
print (" Printing elements in array")
while i < len(nums):
    print (nums[i])
    i += 1
