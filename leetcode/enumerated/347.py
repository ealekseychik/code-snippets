# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurs = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            occurs[num] = 1 + occurs.get(num, 0)

        for num, freq in occurs.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket) - 1, 0, -1):
            if len(bucket[i]) > 0:
                res.extend(bucket[i])
            if len(res) == k:
                return res
