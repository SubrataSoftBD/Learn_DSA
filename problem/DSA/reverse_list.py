from typing import  List

class Solution:
    def reverseList(self, numbers: List[int]) -> List:
        left, right = 0, len(numbers) -1
        while left < right:
            numbers[left], numbers[right] =  numbers[right], numbers[left]

            left += 1
            right -= 1
        return numbers

sol = Solution()
print(sol.reverseList([1, 2, 3, 4, 5]))   # Output: [5, 4, 3, 2, 1]
print(sol.reverseList([10, 20, 30]))     # Output: [30, 20, 10]

#First version: O(n) (new list)

#In-place version: O(1) (no extra list)