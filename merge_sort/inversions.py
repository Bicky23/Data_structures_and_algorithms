# Count the number of inversions in an array

from __future__ import print_function
import sys

## answer
def merge_sort_with_inversions(array):
    # base case
    if len(array) <= 1: return array, 0

    # split into two and recurse
    mid = len(array) / 2
    left, inversions_left = merge_sort_with_inversions(array[:mid])
    right, inversions_right = merge_sort_with_inversions(array[mid:])

    # merge
    sorted_array, inversions_merge = merge(left, right)

    # total inversions = inversions within the left side + inversions within the right side + inversions b/w left and right sides
    inversions = inversions_left + inversions_right + inversions_merge

    return sorted_array, inversions

def merge(left, right):
    merged = list()
    ii, jj = 0, 0
    inversions = 0

    # merge while handling boundary cases for ii, jj reaching end of list
    while ii < len(left) or jj < len(right):
        if ii < len(left) and (jj == len(right) or left[ii] <= right[jj]):
            merged.append(left[ii])
            ii = ii + 1
        else:
            merged.append(right[jj])
            inversions += (len(left)-ii)  # <= count the inversions: right[jj] is smaller than left[ii+1], left[ii+2], .. left[len(left)-1].
            jj = jj + 1

    # just checking that pointers reached the end
    assert ii == len(left), (ii, len(left))
    assert jj == len(right), (jj, len(right))

    return merged, inversions

## input-output
if __name__ == "__main__":
    data = [line.strip() for line in sys.stdin.readlines()][1:]
    for line in data:
        array = [int(xx) for xx in line.split()[1:]]
        sorted_array, inversions = merge_sort_with_inversions(array)
        print(inversions)
