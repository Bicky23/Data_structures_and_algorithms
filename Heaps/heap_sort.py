# calculate index of parent, left child, right child
ROOT = 1
def parent(index):
    return index // 2
def left_child(index):
    return 2*index
def right_child(index):
    return 2*index + 1
 
# Heap() class
class Heap():
    # heap data is stored in self.data
    # first item of self.data is None so that the actual first item is at position 1
    def __init__(self):
        self.data = [None]
 
    def insert(self, element):
        # add element to end of heap
        self.data.append(element)
 
        # upward-swaps
        index = len(self.data)-1
        while index > ROOT:
            # stop if parent is already smaller
            if self.data[parent(index)] < self.data[index]:
                break
 
            # swap with parent
            self.data[parent(index)], self.data[index] = self.data[index], self.data[parent(index)]
            index = parent(index)
 
        return True
 
    def pop(self):
        assert len(self.data) > 1
 
        # store original root
        result = self.data[ROOT]
 
        # move last element to root
        self.data[ROOT] = self.data[-1]
        del self.data[-1]
 
        # downward-swaps
        index = ROOT
        while index < len(self.data):
            left, right = left_child(index), right_child(index)
            if right < len(self.data) and self.data[right] < self.data[index] and self.data[right] < self.data[left]:
                # right child is smaller than parent AND smaller than left child
                # hence, swap with right child
                self.data[right], self.data[index] = self.data[index], self.data[right]
                index = right
            elif left < len(self.data) and self.data[left] < self.data[index]:
                # left child is smaller than parent
                # hence, swap with left child
                self.data[left], self.data[index] = self.data[index], self.data[left]
                index = left
            else:
                break
 
        # return original root
        return result
 
def heap_sort(array):
    heap = Heap()
 
    # insert everything into heap
    for element in array:
        heap.insert(element)
 
    # pop everything from heap
    result = list()
    for ii in range(len(array)):
        element = heap.pop()
        result.append(element)
 
    return result
 
# test
array = [5, 10, 8, 7, 3, 7, 6, 12, 2, 7]
result = heap_sort(array)
print(result)
assert result == [2, 3, 5, 6, 7, 7, 7, 8, 10, 12], result