from typing import List

class Solution:
    def rotate_list(self, numbers: List[int], k: int) -> List:
        n = len(numbers)
        if n == 0:
            return numbers
        k = k % n
        result = []
        print(f"K data: {k}")
        for i in range(n - k, n):
            result.append(numbers[i])
        
        for i in range(0, n - k):
            result.append(numbers[i])
        return result

a = Solution()
print(a.rotate_list([1, 2, 3, 4, 5], 5))        # Output: [4, 5, 1, 2, 3]
print(a.rotate_list([10, 20, 30, 40, 50], 3))   # Output: [30, 40, 50, 10, 20]