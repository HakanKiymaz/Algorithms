def quick_sort(arr):
    """
    Sort the array recursively
    arr: array to be sorted
    """
    if len(arr) <= 1:
        return arr

    pin = arr.pop()
    smaller_arr = []
    greater_arr = []
    for item in arr:
        if item < pin:
            smaller_arr.append(item)
        else:
            greater_arr.append(item)
    return quick_sort(smaller_arr) + [pin] + quick_sort(greater_arr)


if __name__ == "__main__":
    arr = [9, 5, 1, 4, 3, 2, 12, 8, 19]
    print(quick_sort(arr))