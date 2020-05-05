def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list is None:
        return None
    index = 0
    times_added_to_tail = 0
    while index < len(input_list)-1:
        element = input_list[index]
        if element == 0:
            input_list.pop(index)
            input_list.insert(0, element)
        elif element == 2:
            # To prevent looping infinitely when only twos are left at the end of the list. If distance left to the end of
            # the list is smaller than the number of times we added '2' to the end of the list, it means there are only
            # '2's between current element and the end of the list. This means sorting can be finished.
            if times_added_to_tail > len(input_list) - 1 - index:
                break
            input_list.pop(index)
            index -= 1
            input_list.append(element)
            times_added_to_tail += 1
        index += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([1, 2, 0])
test_function([])
test_function([2, 2, 2, 0, 1])
print("Pass" if sort_012(None) is None else "Fail")

