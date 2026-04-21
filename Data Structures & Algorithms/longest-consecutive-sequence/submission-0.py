class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Declare empty set for quick look up
        my_set = set()
        for num in nums:
            my_set.add(num)
        # Declare list to store longest sequence
        sequence = []
        # Loop through set 
        for num in my_set:
            # Check if its a starting point
            if num - 1 not in my_set:
                # Enters here when its a starting point
                # Make temp list to store potential sequence
                temp = []
                # Counter to search for next number in sequence
                i = 0
                while(num + i in my_set):
                    temp.append(num + i)
                    i += 1
                # Check if current sequence is larger than current max sequence
                if len(temp) > len(sequence):
                    sequence = temp
        return len(sequence)