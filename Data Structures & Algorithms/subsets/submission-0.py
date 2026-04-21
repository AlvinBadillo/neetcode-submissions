class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Iterate the list and at every point we have two options
        # Choose the num and add it to the selected subset or not
        # Perhaps we can store all posible combinatios at each index?
        # Or have each new index be the last option with or without the current
        res = [[]]

        for num in nums:
            # List to store new substes
            new_subsets = []
            for subset in res:
                new_subsets.append(subset + [num])
            res.extend(new_subsets)
        return res
                