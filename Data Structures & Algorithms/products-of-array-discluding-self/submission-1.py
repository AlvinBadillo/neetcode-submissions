class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                # Start to fill left, initialize it with a 1
        left = [1] * len(nums)
        right = [1] * len(nums)
        # Loop trough nums and calculate the left multiplication
        for i in range(1, len(nums)):
            left[i] = left[i - 1] * nums[i - 1]
        # Loop trough nums from back to start
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        # Now multiply left[i] with right[i]
        for i in range(len(nums)):
            left[i] = left[i] * right[i]
        return left