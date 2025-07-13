
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return "No data found"
# num = [10, 50, 11, 12, 13]
# print(linear_search(num, 1))



# def linear_search(arr, target):
#     for index, value in enumerate(arr):
#         if value == target:
#             return index
#     return "No data found"
# arr = [5, 3, 7, 8, 7, 1, 9]
# target = 7

# print(linear_search(arr, target))


# def data_exits(arr, target):
#     for data in arr:
#         if data == target:
#             return True
#     return False

# arr = [5, 3, 7, 8, 7, 1, 9]
# print(data_exits(arr, 99))


# def linear_search_all_indices(arr, targets):
#     indices = []
#     for i, value in enumerate(arr):
#         if value == targets:
#             indices.append(i)
#     return indices
# arr = [2, 3, 7, 3, 8,  10]
# print(linear_search_all_indices(arr, 3))

# def linear_search_max(arr):
#     max_val = arr[0]
#     for value in arr[1:]:
#         if value > max_val:
#             max_val = value
#     return max_val

# arr = [1000, 23, 45, 70, 5, 145]
# print(linear_search_max(arr))


# def linear_search_min(arr):
#     min_val = arr[0]
#     for value in arr[1:]:
#         if value < min_val:
#             min_val = value
#     return min_val

# arr = [1000, 23, 45, 70, 5, 145]
# print(linear_search_min(arr))



def char_search(data, target_char):
    for i, ch in enumerate(data):
        if ch == target_char:
            return i
    return "No data found"

s = "Hello World"
print(char_search(s, "Wr "))