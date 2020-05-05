import random

# Max and Min in a Unsorted Array


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers in a single traversal.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None, None

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
l2 = []
l3 = [1, -1, 1, 0]
l4 = [0, 0, 0]

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print("Pass" if ((None, None) == get_min_max(l2)) else "Fail")
print("Pass" if ((-1, 1) == get_min_max(l3)) else "Fail")
print("Pass" if ((0, 0) == get_min_max(l4)) else "Fail")
