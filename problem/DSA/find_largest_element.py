from typing import List


class Solution:
    def findLargestElement(self, numbers: List[int]) -> int:
        if not numbers:
            raise ValueError("This input list is empty")
        largest = numbers[0]
        print(f"Largest Number {largest}")
        for num in numbers:
            if num > largest:
                largest = num
        return largest
    

a = Solution()

# a.findLargestElement([])
a.findLargestElement([1, 4, 3, 21, 234, -1])
print(a.findLargestElement([-1,  -3, -21, -234, -11]))


#Time Complexity: O(n)

#Space Complexity: O(1)

