from typing import List

class Solution:
  def isUnique(self, number: List[int])-> bool:
      for i in range(len(number)):
          for j in range(i + 1, len(number)):
              if number[i] == number[j]:
                  return False
      return True




sol = Solution()
print(sol.isUnique([1, 2, 3, 4, 5]))        # Output: True
print(sol.isUnique([1, 2, 3, 3, 4, 5]))


#Time Complexity: O(n^2) (Brute force)

#Space Complexity: O(1)