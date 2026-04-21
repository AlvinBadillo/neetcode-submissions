class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Declare start and end ponters 
        leftP = 0
        rightP = 1
        # Declare max profit var
        maxP = 0
        # Iterate prices
        while rightP < len(prices): 
            # Check if profitable
            if prices[rightP] > prices[leftP]:
                # Select greatest profit
                maxP = max(maxP, (prices[rightP] - prices[leftP]))
            else:
                # If left pointer is bigger than right pointer, left pointer should be right pointer 
                leftP = rightP
            rightP += 1
        return maxP