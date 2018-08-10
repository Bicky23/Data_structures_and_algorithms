def simple_sort(array):
    n = len(array)
    for i in range(n):
        # compare array[i] with array[i+1], array[i+2], ... array[n-1]
        for j in range(i+1, n):
            # swap if we find a smaller value
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


print(simple_sort([3,5,6,1,2,10,8,15,20,19,25,40,22]))
