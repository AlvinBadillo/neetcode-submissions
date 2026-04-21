class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def house_robber_1(houses):
            prev2, prev = 0, 0
            for n in houses:
                temp = max(n + prev2, prev)
                prev2 = prev
                prev = temp
            return prev
        return max(house_robber_1(nums[1:]), house_robber_1(nums[:len(nums) - 1]))