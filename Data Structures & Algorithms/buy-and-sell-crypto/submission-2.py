class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        index = 1
        lowest = prices[0]

        while index < len(prices):
            curr_profit = prices[index] - lowest
            max_profit = max(max_profit, curr_profit)

            # Update our lowest
            lowest = min(lowest, prices[index])

            index += 1
        return max_profit