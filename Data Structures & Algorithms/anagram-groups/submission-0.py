class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Declare empty result list of list
        result = []
        # Check if strs is empty
        if len(strs) == 0:
            result.append([""])
            return result
        # If it has values add the first one to result
        result.append([strs[0]])
        # Now iterate the rest of strs
        for i in range(1, len(strs)):
            curr = strs[i]
            # Flag to know if we found a list that works
            found = False
            # Check if current word is anagram if any of the current lists
            # If not, add it as a new list
            # Loop through result and see if we find a list that fits current word
            for j in range(len(result)):
                # If we find one, add it to that list
                if self.isAnagram(result[j][0], curr):
                    result[j].append(curr)
                    found = True
                    break
            # If its not in any of the already created lists, add a new one
            if not found:
                result.append([curr])
        return result
            

    def isAnagram(self,str1: str, str2: str):
        # Check if lenght is different
        if len(str1) != len(str2):
            return False
        # Check frequency of letters
        # Declare both hashmaps
        hash1 = {}
        # Populate hash1, key is a letter and value are the times seen
        for char in str1:
            if char in hash1:
                hash1[char] += 1
            else:
                hash1[char] = 1
        # Populate hash2, key is a letter and value are the times seen
        for char in str2:
            if char in hash1:
                hash1[char] -= 1
            else:
                return False 
        # Check if all values are 0
        for value in hash1.values():
            if value != 0:
                return False
        # All counts are zero; the strings are anagrams
        return True