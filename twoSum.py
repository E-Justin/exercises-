nums = [3, 3]

target = 6

# Output: [0,1]


# method to find which two elements in an array to reach the target sum
# method returns indeces of the two elements that when added together, equal the target
def twoSum(nums, target):
    i = 0 
    j = i + 1
    length = len(nums) # get length

    while i < length: # while i is less than length
        if nums[i] + nums[j] == target: # if the sum of the two equals the target
            return [i, j] # return array of indeces 
        else:
            j += 1 # incrememt j
        if j == length: # if j has reached outside of its range in the array
            i += 1 # incrememtn i 
            j = i + 1 # j is one more than i
        if i == (length - 1): # if i has reached outside of its range
            break

print(twoSum(nums, target))
