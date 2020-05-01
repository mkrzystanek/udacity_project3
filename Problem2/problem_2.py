# Search in a Rotated Sorted Array


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Find a point of rotation, which splits list into two sorted lists (time complexity: O(log n))
    rotation_point = find_rotation_point(0, len(input_list)-1, input_list)

    # Find out which list contains searched number (time complexity: O(1))
    start, end = find_array_with_searched_number(input_list, rotation_point, number)

    # Perform binary search on one of the sorted parts of input_lists (time complexity: O(log n)
    return binary_search(input_list, start, end, number)


def find_rotation_point(start, end, input_list):
    mid_point = start + (end - start) // 2
    last_value = input_list[end]
    value = input_list[mid_point]

    if end - start == 1:
        if value > last_value:
            return end
        else:
            return mid_point

    if value < last_value:
        return find_rotation_point(start, mid_point, input_list)
    elif value > last_value:
        return find_rotation_point(mid_point + 1, end, input_list)


def find_array_with_searched_number(input_list, rotation_point, number):
    if rotation_point == 0:
        return 0, len(input_list)-1
    elif input_list[-1] < number:
        return 0, rotation_point-1
    else:
        return rotation_point, len(input_list)-1


def binary_search(input_list, start, end, number):
    if end - start < 0:
        return -1

    mid_point = start + (end - start) // 2
    value = input_list[mid_point]

    if value == number:
        return mid_point
    elif value > number:
        return binary_search(input_list, start, mid_point, number)
    else:
        return binary_search(input_list, mid_point+1, end, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    print("expected: " + str(linear_search(input_list, number)))
    print("output: " + str(rotated_array_search(input_list, number)))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


testList1 = [6, 7, 8, 9, 10, 1, 2, 3, 4]
testList2 = [1, 2, 3, 4, 6, 7, 8, 9, 10]
testList3 = [2, 3, 4, 6, 7, 8, 9, 10, 1]
testList4 = [10, 1, 2, 3, 4, 6, 7, 8, 9]

print("find_rotation_point() tests:")
print(find_rotation_point(0, len(testList1)-1, testList1))
assert find_rotation_point(0, len(testList1)-1, testList1) == 5

print(find_rotation_point(0, len(testList2)-1, testList2))
assert find_rotation_point(0, len(testList2)-1, testList2) == 0

print(find_rotation_point(0, len(testList3)-1, testList3))
assert find_rotation_point(0, len(testList3)-1, testList3) == 8

print(find_rotation_point(0, len(testList4)-1, testList4))
assert find_rotation_point(0, len(testList4)-1, testList4) == 1

print("\nfind_array_with_searched_number tests")
print(find_array_with_searched_number(testList1, 5, 7))
assert find_array_with_searched_number(testList1, 5, 7) == (0, 4)

print(find_array_with_searched_number(testList2, 0, 7))
assert find_array_with_searched_number(testList2, 0, 7) == (0, 8)

print(find_array_with_searched_number(testList3, 8, 7))
assert find_array_with_searched_number(testList3, 8, 7) == (0, 7)

print(find_array_with_searched_number(testList4, 1, 7))
assert find_array_with_searched_number(testList4, 1, 7) == (1, 8)

print("\nbinary_search() tests")
testList5 = [1, 2, 3, 4, 5]
print(binary_search(testList5, 0, len(testList5)-1, 5))
assert binary_search(testList5, 0, len(testList5)-1, 5) == 4

print(binary_search(testList5, 0, len(testList5)-1, 1))
assert binary_search(testList5, 0, len(testList5)-1, 1) == 0

print(binary_search(testList5, 0, len(testList5)-1, 3))
assert binary_search(testList5, 0, len(testList5)-1, 3) == 2

print(binary_search(testList5, 0, len(testList5)-1, 9))
assert binary_search(testList5, 0, len(testList5)-1, 9) == -1

print("\nrotated_array_search() tests")
test_function([testList1, 6])
test_function([testList2, 6])
test_function([testList3, 6])
test_function([testList4, 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
