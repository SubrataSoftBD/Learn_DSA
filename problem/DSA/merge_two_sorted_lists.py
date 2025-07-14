from typing import List
# class Solution:
#     def merge_two_sorted_lists(self, numberOneList : List[int], numberTwoList: List[int]) -> List[int]:
#         i = 0
#         j = 0
#         result = []
#         while i < len(numberOneList) and j < len(numberTwoList):
#             if numberOneList[i] < numberTwoList[j]:
#                 result.append(numberOneList[i])
#                 i += 1
#             else:
#                 result.append(numberTwoList[j])
#                 j += 1
#         print(f"Total Data: {result}")
        
#         # Add any remaining elements
#         while i < len(numberOneList):
#             result.append(numberOneList[i])
#             i += 1
#         while j < len(numberTwoList):
#             result.append(numberTwoList[j])
#             j += 1
#         return result

# sol = Solution()
# print(sol.merge_two_sorted_lists([1, 3, 5, 10, 50], [2, 4, 6, 70]))

def merge_two_sorted_lists(numberOneList : List[int], numberTwoList: List[int]) -> List[int]:
    i = 0
    j = 0
    result = []
    while i < len(numberOneList) and j < len(numberTwoList):
        if numberOneList[i] < numberTwoList[j]:
            result.append(numberOneList[i])
            i += 1
        else:
            result.append(numberTwoList[j])
            j += 1
    print(f"Total Data: {result}")

    # Add any remaining elements
    while i < len(numberOneList):
        result.append(numberOneList[i])
        i += 1
    while j < len(numberTwoList):
        result.append(numberTwoList[j])
        j += 1
    return result

list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_two_sorted_lists(list1, list2))