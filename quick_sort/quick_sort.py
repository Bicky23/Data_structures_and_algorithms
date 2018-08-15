import random

def quick_sort(array):
    # three arrays
    less, equal, greater = [], [], []
    if len(array) > 1:
        # pivot element
        pivot = array[random.randint(0, len(array)-1)]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return quick_sort(less) + equal + quick_sort(greater)
    # base case
    else:
        return array
