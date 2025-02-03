# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        rotations = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                rotations += 1

        if nums[0] < nums[-1]:
            rotations += 1
        return rotations <= 1
