# https://leetcode.com/problems/find-k-th-smallest-pair-distance/

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]

        while low < high:
            mid = (low + high) // 2
            count = 0
            left = 0

            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left

            if count >= k:
                high = mid
            else:
                low = mid + 1

        return low
