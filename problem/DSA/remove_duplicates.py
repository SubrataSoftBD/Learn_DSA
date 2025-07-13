from typing import List

class Solution:
    def removeDuplicates(self, number: List[int])-> List:
        result = []
        for num in number:
            exists = False
            for res in result:
                if res == num:
                    exists = True
                    break
            if not exists:
                result.append(num)
        return result

sol = Solution()
print(sol.removeDuplicates([1, 2, 2, 3, 4, 4, 5]))    # Output: [1, 2, 3, 4, 5]
print(sol.removeDuplicates([4, 5, 5, 4, 6, 7]))       # Output: [4, 5, 6, 7]
print(sol.removeDuplicates([]))   

#Time Complexity: O(n^2)
#(কারণ প্রতি উপাদানের জন্য আমরা result-এর ভিতর লুপ চালাচ্ছি)

#Space Complexity: O(n)
#(নতুন লিস্টে ইউনিক উপাদান রাখছি)