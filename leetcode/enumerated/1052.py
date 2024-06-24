# https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        min_val = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                min_val += customers[i]

        max_val = min_val
        for i in range(len(customers) - minutes + 1):
            curr = 0
            for j in range(minutes):
                if grumpy[i+j]:
                    curr += customers[i+j]
            
            max_val = max(min_val + curr, max_val)

        return max_val
