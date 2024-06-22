# https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_counts = {0: 1}
        current_prefix_sum = 0
        count = 0

        for num in nums:
            current_prefix_sum += num % 2

            if current_prefix_sum - k in prefix_counts:
                count += prefix_counts[current_prefix_sum - k]

            if current_prefix_sum in prefix_counts:
                prefix_counts[current_prefix_sum] += 1
            else:
                prefix_counts[current_prefix_sum] = 1

        return count
