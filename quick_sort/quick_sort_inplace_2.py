import random

# Hoare partition scheme
def quicksort(array, low=0, high=None):
    # allow high=None, so that quick_sort(array) sorts the entire array
    if high is None:
        high = len(array)-1
    # nothing to sort if low = high (only 1 element)
    if low >= high:
        return array
    # pick a pivot
    pivot = array[random.randint(low, high)]
    # partition
    left, right = low, high
    # loop forever
    while True:
        # move the pointers
        while left < len(array) and array[left] < pivot:
            left += 1
        while right >= 0 and array[right] > pivot:
            right -= 1
        # check if partition is complete
        if left >= right:
            break
        # swap
        array[left], array[right] = array[right], array[left]
        # increment and decrement
        left += 1
        right -= 1

    quicksort(array, low=low, high=right)
    quicksort(array, low=right+1, high=high)

    return array
