class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for num in nums]
        pre_fix = 1
        for i in range(len(nums)):
            res[i] = pre_fix
            pre_fix = pre_fix * nums[i]
        # print(res)
        # now same thing, backwards
        post_fix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * post_fix
            post_fix = post_fix * nums[i]
        # print(res)
        return res



