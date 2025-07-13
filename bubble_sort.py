import time
import os

def print_array(arr, highlight_indices=None):
    os.system('cls' if os.name == 'nt' else 'clear')  # Console পরিষ্কার (Windows/Linux/macOS)

    for i in range(len(arr)):
        val = f"{arr[i]:>3}"
        if highlight_indices and i in highlight_indices:
            print(f"[{val}]", end=' ')  # highlight করা উপাদান
        else:
            print(f" {val} ", end=' ')
    print("\n")

def bubble_sort_visual(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            print_array(arr, highlight_indices=[j, j+1])
            time.sleep(0.5)

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print_array(arr, highlight_indices=[j, j+1])
                print("Swapped!")
                time.sleep(0.5)

    print_array(arr)
    print("✅ Sorting Complete!")

# উদাহরণ অ্যারে
arr = [64, 34, 25, 12, 22, 11, 90]

# সোর্ট শুরু
bubble_sort_visual(arr)



# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]


# arr = [64, 34, 25, 12, 22, 11, 90]


# bubble_sort(arr)
# print("Sorted array:", arr)