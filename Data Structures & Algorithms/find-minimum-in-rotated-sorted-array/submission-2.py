class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Declare left and right pointers
        left, right, minimum = 0, len(nums) - 1, nums[0]
        while left <= right:
            middle = (right + left) // 2
            print('left: ', nums[left], ' middle: ', nums[middle], ' right: ', nums[right])
            minimum = min(minimum, nums[middle])
            print('Min: ', minimum)
            if nums[middle] >= nums[left]:
                minimum = min(nums[left], minimum)
                print('Keeping right')
                # Want to keep the right side
                left = middle + 1
                
            else:
                print('Keeping left')
                minimum = min(nums[right], minimum)
                # Keep left side
                right = middle - 1
                
        return minimum
