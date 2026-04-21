class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                # Iterate list, and checj if there is a number in the hashmap
        # that when added to current num equals the target sum
        # The key of the dictionary is the number and the value is the index
        my_dict = dict()
        for i in range(len(nums)):
            wanted = target - nums[i]
            if wanted in my_dict:
                # If it exists return index of current and index of wanted
                return [my_dict[wanted], i]
            else:
                my_dict[nums[i]] = i
