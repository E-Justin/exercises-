# Write a function that reverses a string. The input string is given as an array of characters s

s = ["J","u","s","t","i","n"]
length = len(s)

def reverseString(s):
    
    i = 0
    j = length -1

    while i < length / 2:
        front = s[i]
        back = s[j]
        s[i] = back
        s[j] = front
        i += 1
        j -= 1
    return s

reverseString(s)

i = 0
while i < length:
    print(s[i])
    i += 1
    
# or .........

def reverseString2(str):
    str = str[::-1]
    return str

# or .......
def reverseTheArray(arr):
    length = len(arr)
    half = length // 2

    front = 0
    back = -1

    while front < half:
        arr[front], arr[back] = arr[back], arr[front]
        front += 1
        back -= 1
    
    return arr

# or ........

def alpha_sort(a_list: list) -> list:
    length = len(a_list) - 1  # length / last available index

    for i in range(length):  # iterate through list one time for each item
        list_changed = False  # flag to let program know that changes were or were not made
        for j in range(length):  # iterate through previous for loop (length * length) times
            current = a_list[j]  # get item
            after = a_list[j + 1]  # get item next to current

            if current > after:  # if items are in descending order
                a_list[j], a_list[j + 1] = a_list[j+1], a_list[j]  # switch them
                list_changed = True  # flag to let program know that changes were made
        if list_changed is False:  # if no changes were made
            break  # exit loop

    return a_list  # return sorted list




# runtime: 203 ms
# memory usage: 21.2MB
