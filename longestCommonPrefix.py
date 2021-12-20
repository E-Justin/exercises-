# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
    prefix = "" # empty string to retrun if there is no common prefix

    strs = sorted(strs) # sorts array

    first = strs[0] # gets first word
    l1 = len(first)
    last = strs[-1] # gets last word
    l2 = len(last)

    i = 0
    if l1 >= l2:
        while i < l2 and first[i] == last[i]: # if the indexed letters are the same in each word
            prefix += first[i] # concatenate string one char at a time
            i += 1 # move to next letter
    if l1 < l2:
        while i < l1 and first[i] == last[i]: # if the indexed letters are the same in each word
            prefix += first[i] # concatenate string one char at a time
            i += 1 # move to next letter

    return prefix

prefix = longestCommonPrefix(strs)

print (prefix)
