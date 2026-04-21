class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        my_set = set(nums)
        # helper
        def count_sequence(n):
            count = 1
            while True:
                if n + 1 in my_set:
                    count += 1
                    n += 1
                else:
                    return count

        for num in nums:
            # first validate if its a posible time
            if num - 1 not in my_set:
                # if its not in the set, this is a valid starting point
                temp = count_sequence(num)
                # asing res to highest number 
                res = max(res, temp)
        return res

            

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4