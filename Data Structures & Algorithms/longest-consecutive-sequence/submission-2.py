class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Make a set identical to nums, this will allow O(1) lookups
        my_set = set(nums)
        result = 0
        # Now iterate nums
        for num in nums:
            # Check if num is a potential starting point 
            if (num - 1) not in my_set:
                # If its a starting point, check how long it goes
                j = 1
                temp = 1
                while(True):
                    if (num + j) in my_set:
                        temp += 1
                        j += 1
                    else:
                        break
                if temp > result:
                    result = temp
        return result