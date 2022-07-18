def bubble_sort(arr):
    for i in range(len(arr)):
        is_sorted = True
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False
        if is_sorted:
            break
    return arr


if __name__ == "__main__":
    arr = [1, 2, 6, 8, 3, 1, 8, 0, 2, 1, 6]
    print(bubble_sort(arr))