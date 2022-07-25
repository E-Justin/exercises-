def bubble_sort(the_list):
    last = len(the_list) - 1  # last index in the list

    for i in range(last):  #  loop cycles through 4 times
        list_changed = False  #  list has not been changed yet
        for j in range(last):  # loop cycles through 4 times for each iteration of the previous loop
            item = the_list[j]  #  get the next two items
            next = the_list[j+1]  # get the next two items

            if item > next:  # if they are in descending order
                #  switch them
                the_list[j] = next  
                the_list[j+1] = item
                list_changed = True  # list changed

            print(the_list, i, j)  # show the list changing through each iteration
        print(list_changed)  # show if the list changed or not
        if list_changed == False:  # if no changes were made to the list
            break  # exit loop (it is sorted)
