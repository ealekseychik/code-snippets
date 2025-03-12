# https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_n = float("inf")
        mid_n = float("inf")
        for i in nums:
            if i <= min_n:
                min_n = i
            elif i <= mid_n:
                mid_n = i
            else:
                return True

        return False