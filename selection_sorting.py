def selection_sort(arr):
    if len(arr) <= 1:
        return arr
    min_index = 0
    minimum = arr[min_index]
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
            min_index = i
    arr[0], arr[min_index] = arr[min_index], arr[0]
    arr.pop(0)
    return [minimum] + selection_sort(arr)


if __name__ == "__main__":
    import random
    arr = [random.randint(1, 100000) for i in range(100)]
    print(selection_sort(arr))