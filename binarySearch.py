def binarySearchA(list, find):
    list.sort() # sort list in ascending order
    first = 0 # start at the beginning index
    length = len(list) # get length
    last = length - 1 # last index of the list
    found = False 

    while first <= last:
        mid = (first + last) // 2 # get middle of the list and truncate the decimal if needed through integer division
        if list[mid] == find: # if value has been found
            found = True
            break
        else:
            if find < list[mid]: # if the value to be found is less than the current indexed value
                last = mid - 1
            else: # if the value to be found is greater than the current indexed value
                first = mid + 1
    return found
