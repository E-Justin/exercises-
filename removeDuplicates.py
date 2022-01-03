 # remove duplicates from array and return length (k)

nums = [0,0,1,1,1,2,2,3,3,4]


def removeDuplicates(nums):
    k = len(nums) # get length
    i = 0

    while i < k:
        look4 = nums[i] # value to search for
        k = len(nums) # update length 
        if nums.count(look4) > 1: # if more than one of the same value is found
            nums.remove(look4) # remove it
        else:
            i += 1 # move to the next index

    k = len(nums) # update length
    return k # return the length of the array after removing duplicates

removeDuplicates(nums)

# Runtime: 2652 ms
# Memory Usage: 14.5 MB




# or 
def removeDuplicates2(numArray):
  k = len(numArray) # get length
  i = 1
  j = i -1

  while i < k: # while i is in range
     if numArray[i] == numArray[j]: # if they are the same
         numArray.remove(numArray[i]) # remove one
         k -= 1 # update length after removing an element
     else:
         i += 1 # increment i
         j = i - 1 # increment j
        
  return k # return length
  
