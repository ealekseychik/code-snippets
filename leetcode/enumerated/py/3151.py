# https://leetcode.com/problems/special-array-i/

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = len(nums)
        if l == 1:
            return True

        for i in range(l - 1):
            if (nums[i] + nums[i+1]) % 2 == 0:
                return False

        return True
