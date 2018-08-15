def merge_sort_inversions(array):
    # base case
    if len(array) <= 1: return array, 0

    # split into two and recurse
    mid = len(array) // 2
    left, left_inversions = merge_sort_inversions(array[:mid])
    right, right_inversions = merge_sort_inversions(array[mid:])

    # merge and return
    sorted_array, inversions = merge(left, right)

    return sorted_array, inversions + left_inversions + right_inversions


# easiest to understand merge() function
def merge(left, right):
    # empty merged list
    merged = []
    inversions = 0
    ''' For both the sorted lists, compare their first element,
    then remove the element which is smaller and put it in the merged list '''
    while len(left) and len(right):
        if left[0] <= right[0]:
            merged.append(left[0])
            left.pop(0)
        else:
            merged.append(right[0])
            right.pop(0)
            inversions += 1

    # check for remaining values in left
    if len(left):
        merged.extend(left)
    # check for remaining values in right
    if len(right):
        merged.extend(right)
    return merged, inversions


array = [3,3,1,4]
result = merge_sort_inversions(array)
print(result)
