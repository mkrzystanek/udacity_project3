class HeapSort:
    def __init__(self, input_list):
        self.heap_list = input_list
        self.create_heap()

    def create_heap(self):
        for index in range(len(self.heap_list), -1, -1):
            self.heapify(index)

    def heapify(self, index):
        left_child_index = 2 * index
        right_child_index = 2 * index + 1
        largest = index

        if left_child_index < len(self.heap_list) and self.heap_list[left_child_index] > self.heap_list[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap_list) and self.heap_list[right_child_index] > self.heap_list[largest]:
            largest = right_child_index

        if largest != index:
            temp = self.heap_list[index]
            self.heap_list[index] = self.heap_list[largest]
            self.heap_list[largest] = temp
            self.heapify(largest)

    def remove_largest(self):
        if self.size() > 1:
            removed = self.heap_list.pop(0)
            self.heap_list.insert(0, self.heap_list.pop(-1))
            self.heapify(0)
            return removed
        elif self.size() == 1:
            return self.heap_list.pop()
        return -1

    def size(self):
        return len(self.heap_list)


if __name__ == "__main__":
    test_list1 = [1, 2, 3, 4, 5]
    heapSort = HeapSort(test_list1)
    print(heapSort.heap_list)
    print(heapSort.remove_largest())
    print(heapSort.heap_list)
    print(heapSort.remove_largest())
    print(heapSort.heap_list)
    print()

    test_list2 = [3, 1, 6, 2, 7]
    heapSort2 = HeapSort(test_list2)
    print(heapSort2.heap_list)
    print(heapSort2.remove_largest())
    print(heapSort2.heap_list)
    print(heapSort2.remove_largest())
    print(heapSort2.heap_list)
    print(heapSort2.remove_largest())
    print(heapSort2.heap_list)
    print(heapSort2.remove_largest())
    print(heapSort2.heap_list)
    print()

    test_list3 = [1]
    heapSort3 = HeapSort(test_list3)
    print(heapSort3.remove_largest())
    print(heapSort3.heap_list)
    print(heapSort3.remove_largest())
    print(heapSort3.heap_list)
