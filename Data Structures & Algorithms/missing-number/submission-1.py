class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSum, maxSum = 0, 0
        # Calculte maxSum
        for i in range(len(nums) + 1):
            maxSum += i
        # Calculate numsSum
        for num in nums:
            numsSum += num
        # Return difference
        return maxSum - numsSum