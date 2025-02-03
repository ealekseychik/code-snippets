# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        decLen = 1
        incLen = 1
        maxLen = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                decLen = 1
                incLen += 1
            elif nums[i] > nums[i+1]:
                decLen += 1
                incLen = 1
            else:
                decLen = 1
                incLen = 1

            maxLen = max(decLen, incLen, maxLen)

        return maxLen
