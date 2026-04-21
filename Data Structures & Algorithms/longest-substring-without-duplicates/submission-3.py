class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Set up left pointer, set and res
        left, res = 0, 0
        my_set = set()
        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(s[r])
            res = max(res, r - left + 1)
        return res