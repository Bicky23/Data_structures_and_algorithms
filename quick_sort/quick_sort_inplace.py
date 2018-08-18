import random

# Lomuto partition scheme

def partition(array, low=0, high=None):

    if high == None:
        high = len(array) - 1
    # chose pivot to be the last element of the array
    pivot = array[high]
    # maintaining index
    i = low
    # index to loop over the array
    for j in range(low, high):
        if array[j] < pivot:
            # swap places
            array[j], array[i] = array[i], array[j]
            # increment maintaining index by 1
            i += 1
    # swap pivot with maintaining index to divide into two halves
    array[high], array[i] = array[i], array[high]
    # return pivot for next partition
    return i


def quicksort(array, low, high):
    if low < high:
        index = partition(array, low, high)
        quicksort(array, low, index-1)
        quicksort(array, index+1, high)
    return array


print(quicksort([1,2,3,4,6,10,8,100,26,57,78,35], 0, 11))
