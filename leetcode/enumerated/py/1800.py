# https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = nums[0]
        currentSum = result
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                currentSum += nums[i]
            else:
                currentSum = nums[i]

            result = max(currentSum, result)
        
        return result