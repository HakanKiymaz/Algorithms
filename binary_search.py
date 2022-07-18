def binary_search(array, x, lower_bound=None, upper_bound=None):
    """
    array: the list sorted in ascending
    x: the value that we search for index
    return: if x in the list reutrns index of x, else -1
    """
    if not lower_bound:
        lower_bound = 0
    if not upper_bound:
        upper_bound = len(array) - 1
    if upper_bound >= lower_bound:
        mid_point = lower_bound + (upper_bound - lower_bound) // 2
        if array[mid_point] == x:
            return mid_point
        elif array[mid_point] > x:
            return binary_search(array, x, lower_bound, mid_point - 1)
        else:
            return binary_search(array, x, mid_point + 1, upper_bound)
    else:
        return -1


if __name__ == "__main__":
    ar = [1, 2, 3, 4, 5, 6, 7, 8, 19, 23, 29, 32, 66, 68]
    x = 6
    print(binary_search(ar, x))
