class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # I can check if the lengths are the same, if they aren't return false
        if len(s) != len(t):
            return False
        # Declare dictionary
        dict1 = dict()
        # Loop over both words 
        for i in range(len(s)):
            # Add one to value 
            dict1[s[i]] = dict1.get(s[i], 0) + 1
            # Remove one from value
            dict1[t[i]] = dict1.get(t[i], 0) - 1

        # Loop through dict1, if we find all 0's return true, else return false
        for value in dict1.values():
            if value != 0:
                return False
        return True