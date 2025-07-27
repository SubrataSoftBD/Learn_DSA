def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n):
        for j in range(0, n - 1 - i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j + 1], arr[j]

    return arr

unsorted_arr = [5, 4, 6, 2, 1]

sorted_list = bubble_sort(unsorted_arr)

print(f"Sorted array: {sorted_list}")