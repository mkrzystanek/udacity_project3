import random

# Max and Min in a Unsorted Array


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers in a single traversal.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_value = float("inf")
    max_value = float("-inf")
    for i in ints:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i
    return min_value, max_value


# Example Test Case of Ten Integers

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
