# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]
        max_sum = 0

        for price in prices:
            if price > prev:
                max_sum += price - prev

            prev = price

        return max_sum
