class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the approach will be to first sort all string
        # then the sorted version of the string will be the the key, and the value will be 
        # a list of all the unsorted words
        # the key here is that the sorted words are the same if they are anagrams
        sort_strs = {}
        for word in strs:
            s_word = "".join(sorted(word))
            if s_word in sort_strs:
                sort_strs[s_word].append(word)
            else:
                sort_strs[s_word] = [word]
        
        return list(sort_strs.values())