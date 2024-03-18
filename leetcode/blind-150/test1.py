# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, arr: List[int]) -> bool:
        return len(set(arr)) < len(arr)
