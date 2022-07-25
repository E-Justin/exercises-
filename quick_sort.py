
def sort_part(the_list: list, low_index: int, pivot_index: int)-> int:
    pivot_val = the_list[pivot_index]  # get pivot value (last item in the list)

    while pivot_index != low_index:  # while pivot index is different than low index
        low_val = the_list[low_index]  # get lowest index val

        print(the_list, low_val, pivot_val)  #?  for testing
        if low_val <= pivot_val:  #! if these two are already sorted correctly
            low_index += 1  # move to the next one
        else:  #! if these two are not already sorted
            the_list[low_index] = the_list[pivot_index - 1]  # move item to the left of pivot value to the front
            the_list[pivot_index] = low_val  # move the first value to where the pivot is
            the_list[pivot_index - 1] = pivot_val  # move pivot value to the left by 1
            pivot_index -= 1  # decrement pivot index by 1

    return pivot_index  # return pivot index


def quick_sort(the_list: list, low_index: int, high_index: int):
    if low_index > high_index: 
        return

    pivot_index = sort_part(the_list, low_index, high_index)
    quick_sort(the_list, low_index, pivot_index - 1)
    quick_sort(the_list, pivot_index + 1, high_index)


quick_sort(my_list, 0, len(my_list) - 1)
print('my_list : ', my_list)
