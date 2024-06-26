# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        longest = 0
        for num in nums:
            if num - 1 not in nums:
                current = 1
                while num + 1 in nums:
                    num += 1
                    current += 1

                longest = max(longest, current)

        return longest
