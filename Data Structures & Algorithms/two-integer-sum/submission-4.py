class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)):
            curr = nums[i]
            complement = target - curr
            if complement in my_dict:
                return [my_dict[complement], i]
            my_dict[curr] = i