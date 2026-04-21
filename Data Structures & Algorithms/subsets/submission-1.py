class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # To return all subsets we have two options at every step
        # Choose the number we are currently at or not
        res = [[]]

        def dfs(i):
            # Base case, if we reach the end of the list
            if i >= len(nums):
                return
            new_subsets = []
            for subset in res:
                new_subsets.append(subset + [nums[i]])
            res.extend(new_subsets)
            dfs(i+1)
        dfs(0)
        return res