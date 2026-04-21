class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # build a letter dictionary where letter -> ocurrances
        # dictionary is at most 26 (one per letter)
        # if dictionaries are the same return true
        dict1 = {}
        for letter in s:
            if letter in dict1:
                dict1[letter] += 1
            else:
                dict1[letter] = 1
        dict2 = {}
        for letter in t:
            if letter in dict2:
                dict2[letter] += 1
            else:
                dict2[letter] = 1
        return dict1 == dict2


