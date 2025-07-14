from typing import List
class Solution:
    def maxConsecutiveDiff(self, number: List[int]) -> int:
        if len(number) < 2:
            return 0
        max_diff = 0
        for i in range(len(number) - 1):
            a = number[i]
            b = number[i + 1]
            print(f"A: {a}")
            print(f"B: {b}")
            if a > b:
                diff = a - b
            else:
                diff = b - a
            if diff > max_diff:
                max_diff = diff
        return max_diff

sol = Solution() # type: ignore
print(sol.maxConsecutiveDiff([1, 7, 3, 10, 5]))  # Output: 7
print(sol.maxConsecutiveDiff([10, 11, 15, 3]))   # Output: 12
print(sol.maxConsecutiveDiff([5])) 


#Time: O(n)

#Space: O(1)