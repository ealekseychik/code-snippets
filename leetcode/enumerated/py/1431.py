# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/ 

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_default = 0
        for i in candies:
            max_default = max(max_default, i)

        res = []
        for i in candies:
            res.append(i + extraCandies >= max_default)

        return res
