from typing import List
# def sum_of_list(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return print(total)


# sum_of_list([1,2,3,4,5,6])

class Solution:

    def sum_of_list(self, numbers: List[int]) -> int:
        total = 0
        for num in numbers:
            total += num
        return print(total)
    

a = Solution()


a.sum_of_list([1,2,3,6,9,8,7])


#Time Complexity: O(n) — প্রতিটি এলিমেন্ট ১ বার পড়ছে

#Space Complexity: O(1) — অতিরিক্ত কোনো জায়গা লাগছে না