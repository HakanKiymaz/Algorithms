def insertion_sort_asc(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        prev_index = i - 1
        while prev_index >= 0 and current_value < arr[prev_index]:
            arr[prev_index + 1] = arr[prev_index]
            prev_index -= 1
        arr[prev_index + 1] = current_value
    return arr


def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        prev_index = i - 1
        while prev_index >= 0 and current_value > arr[prev_index]:
            arr[prev_index + 1] = arr[prev_index]
            prev_index -= 1
        arr[prev_index + 1] = current_value
    return arr


if __name__ == "__main__":
    data = [2, 9, 5, 1, 4, 3]
    print(insertion_sort_asc(data))
    data = [2, 9, 5, 1, 4, 3]
    print(insertion_sort_desc(data))