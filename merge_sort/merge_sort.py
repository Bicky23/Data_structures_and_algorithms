def merge_sort(array):
    # base case
    if len(array) <= 1: return array

    # split into two and recurse
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # merge and return
    return merge(left, right)

# easiest to understand merge() function
def merge(left, right):
    # empty merged list
    merged = []
    ''' For both the sorted lists check compare the first elements
    then remove the element which is smaller and put it in the merged list '''
    while len(left) and len(right):
        if left[0] <= right[0]:
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            right.pop(0)

    # check for remaining values in left
    if len(left):
        merged.extend(left)
    # check for remaining values in right
    if len(right):
        merged.extend(right)
    return merged


array = [5, 10, 8, 7, 3, 7, 6, 12, 2, 7]
result = merge_sort(array)
print(result)
assert result == [2, 3, 5, 6, 7, 7, 7, 8, 10, 12], result
