from typing import List
class Solution:
    def rectangle_pattern(self, n: int, m: int) -> List[str]:
        result = []
        row = "*" * m
        for _ in range(n):
            result.append(row)
        return result
a = Solution()
print(a.rectangle_pattern(15, 5))