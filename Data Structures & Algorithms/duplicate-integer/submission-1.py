class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # declare set
        my_set = set()
        # If value is already in set return true
        for num in nums:
            if num in my_set:
                return True
            else:
                # If not, add it to the set
                my_set.add(num)
        # If we exit the loop return False
        return False