# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if min_price > price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
