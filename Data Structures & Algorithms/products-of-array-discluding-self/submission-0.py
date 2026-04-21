class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Declare both lists and give them the same size as nums
        left = [None] * len(nums)
        right = [None] * len(nums)
        # First value of left is 1
        left[0] = 1
        # Now fill left -> left[i] = left[i-1] * nums[i-1]
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i -1]
        # Now fill right
        # Last value is always 1
        right[len(nums) -1] = 1
        # Iterate from right to left 
        # right[i] = right[i + 1] * nums[i +1]
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        # Now to build the final result
        # result[i] = left[i] * right[i] 
        result = [None] * len(nums)
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
        return result
        