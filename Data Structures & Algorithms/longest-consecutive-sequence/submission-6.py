class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set()
        for num in nums:
            my_set.add(num)
        
        max_sequence = 0
        for num in my_set:
            if num - 1 not in my_set:
                # compute the size of this sequence
                curr_sequence = 0
                for i in range(len(nums)):
                    if num + i in my_set:
                        curr_sequence += 1
                    else:
                        break
                max_sequence = max(max_sequence, curr_sequence)

        return max_sequence
