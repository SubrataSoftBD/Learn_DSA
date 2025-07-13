
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        # mid =  right // 2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            left = mid + 1
        else:
            right = mid - 1
    return "No data found"

# arr = [10, 20, 30, 40, 50, 60, 70]


# print(binary_search(arr, 40)) 

arr = list(range(0, 1001, 10))  # [0, 10, 20, ..., 1000]
target =77

print( binary_search(arr, target))

