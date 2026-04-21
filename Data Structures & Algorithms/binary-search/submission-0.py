class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search:
        # Find middle of the list and check the following:
        # - If curr == target: return curr
        # - if curr < target: keep right side
        # - if curr > target: keep left side
        left, right = 0, len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1