from typing import List, Tuple
class Solution:
    def countEvenOdd(self, numbers: List[int]) -> Tuple[int, int]:
        even_count = 0
        odd_count = 0
        even_list = []
        odd_list = []
        
        for num in numbers:
            if num % 2 == 0:
                even_list.append(num)
                even_count += 1
            else:
                odd_list.append(num)
                odd_count += 1
        print(f"Even number is: {even_list}")
        print(f"Odd number is: {odd_list}")
        return (even_count, odd_count)
sol = Solution()
print(sol.countEvenOdd([1, 2, 3, 4, 5]))     # Output: (2, 3)
print(sol.countEvenOdd([10, 20, 30]))        # Output: (3, 0)
print(sol.countEvenOdd([1, 3, 5, 7]))        # Output: (0, 4)


#Time Complexity: O(n) – লিস্টের প্রতিটি উপাদান একবার করে দেখা হয়।

#Space Complexity: O(1) – আমরা শুধু দুটি কাউন্টার ব্যবহার করছি।