#BubbleSort
import random
def get_unsorted_list(amount_of_numbers):
    unsorted_list = []
    for i in range(amount_of_numbers):
        unsorted_list.append(random.randint(1,10)) 
    return unsorted_list

print get_unsorted_list(10)

def bubble_sort(unsorted_list):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(1,len(unsorted_list)):
            if unsorted_list[i-1] > unsorted_list[i]:
                swapped = True
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i-1]
                unsorted_list[i-1] = temp
    return unsorted_list

print bubble_sort(get_unsorted_list(10))
