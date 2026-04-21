class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use built in way to make set
        my_set = set(nums)
        # Store length of max squence
        max_sequence = 0
        # Loop through set 
        for num in my_set:
            # Check if its a starting point
            if num - 1 not in my_set:
                # Enters here when its a starting point
                # Store length of curr sequcne
                temp = 0
                # Counter to search for next number in sequence
                i = 0
                while(num + i in my_set):
                    temp += 1
                    i += 1
                max_sequence = max(max_sequence, temp)
        return max_sequence