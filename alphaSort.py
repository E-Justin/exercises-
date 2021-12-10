# sort an array of chars in alphabetical order without using library function

unSorted = ["z", "h", "b", "k", "a", "q", "s", "o"]

def alphaSort(unSorted):
    index = 0
    check = 1
    length = len(unSorted)
    insert = 0

    while index < length and check < length:
        if unSorted[index] > unSorted[check]:
            before = unSorted[check]
            after = unSorted[index]
            unSorted[index] = before
            unSorted[check] = after
        check += 1
        if check == length:
            index += 1
            check = index +1
            insert += 1
    return unSorted 

alphaSort(unSorted)

index = 0
while index < len(unSorted):
    print (unSorted[index])
    index += 1
