class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Case where we only have one price
        if len(prices) == 1:
            return 0
        # Set up window and profit variable
        i, j, max_profit = 0, 1, 0
        while(j < len(prices) and i < j):
            # Calculate current profit
            curr_profit = prices[j] - prices[i]
            # Replace max_profit with the largest of the two
            max_profit = max(max_profit, curr_profit)
            # Move window
            if prices[i] < prices[j]:
                j += 1
            else:
                i += 1
                if i == j:
                    j = i + 1
        return max_profit       