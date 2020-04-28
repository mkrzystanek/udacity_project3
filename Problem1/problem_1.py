# Finding the Square Root of an Integer


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 1:
        return 1
    if number == 0:
        return 0

    return _sqrt(0, number, number)


def _sqrt(start, end, number):
    middle_point = (end - start) // 2 + start

    if middle_point * middle_point == number:
        return middle_point
    elif middle_point * middle_point > number:
        if end - start <= 2:
            return middle_point - 1
        return _sqrt(start, middle_point, number)
    else:
        if end - start <= 2:
            return middle_point
        return _sqrt(middle_point, end, number)


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(25)) else "Fail")
print(sqrt(27))
print("Pass" if (5 == sqrt(27)) else "Fail")
print(sqrt(30))
print("Pass" if (5 == sqrt(30)) else "Fail")
print(sqrt(15))
print("Pass" if (3 == sqrt(15)) else "Fail")
print("Pass" if (1 == sqrt(2)) else "Fail")
print("Pass" if (3 == sqrt(14)) else "Fail")
print("Pass" if (2 == sqrt(7)) else "Fail")
