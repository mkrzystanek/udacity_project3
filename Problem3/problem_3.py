from HeapSort import HeapSort

# Rearrange Array Elements


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Create a max heap of input list O(n)
    heap = HeapSort(input_list)
    # Create two output strings, that will represent returned values O(1)
    first_number = "0"
    second_number = "0"
    # Remove max value from the heap, and add it to one of the output lists. O(log n)
    # Then repeat for the second output list. O(log n)
    # Time complexity of the loop: O(n log n)
    should_add_to_first_list = True
    while heap.size() > 0:
        max_elem = heap.remove_largest()
        if should_add_to_first_list:
            first_number += str(max_elem)
        else:
            second_number += str(max_elem)
        should_add_to_first_list = not should_add_to_first_list
    # Change output strings to numbers and return
    return [int(first_number), int(second_number)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(output)
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_case2 = [[], [0, 0]]
test_function(test_case2)
test_case3 = [[1], [1, 0]]
test_function(test_case3)
test_case4 = [[0], [0, 0]]
test_function(test_case4)
test_case5 = [None, [0, 0]]
test_function(test_case5)
