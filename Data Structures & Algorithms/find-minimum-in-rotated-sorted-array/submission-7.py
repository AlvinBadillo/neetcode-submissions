class Solution:
    def findMin(self, nums: List[int]) -> int:
        # I only care aboute the min so i just need a singe var to store it
        # simple answer is to loop throught the array and be done with it
        # But how can i explait the fact that it had been sorted
        # But rotated by k times
        # Im thinking we can maybe have 3 pointers
        # Left, Middle, Right
        # Now based on these I think we can basically pinpoint where the "start" of the original sorted array is
        # if left > middle -> our smalles number is on the left
        # if right < middle -> smalles number is on the right

        left, right = 0, len(nums) - 1
        min_num = nums[0]
        while left <= right:
            mid = (right + left) // 2
            print(mid)
            min_num = min(min_num, nums[mid])
            # check where the smaller numbers are
            if nums[mid] < nums[right]:
                # then the smaller numbers are to the left
                right = mid - 1
            else:
                # the min is to the right
                left = mid + 1
        return min_num


        # Input: nums = [3,4,5,6,1,2]
        #                L   M     R
        # 
        # 