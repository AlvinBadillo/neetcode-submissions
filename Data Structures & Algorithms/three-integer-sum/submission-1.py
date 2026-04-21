class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort nums
        nums.sort()
        # Decalre res
        res = []
        # Set up main loop
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i != 0:
                continue
            curr = nums[i]
            left, right = i + 1, len(nums) - 1
            while(left < right):
                sum = curr + nums[left] + nums[right]
                if sum == 0:
                    res.append([curr, nums[left], nums[right]])
                    left += 1
                    while(nums[left] == nums[left-1] and left < right):
                        left += 1                    
                elif sum > 0:
                    right -= 1
                else:
                    # Sum < 0
                    left += 1
        return res