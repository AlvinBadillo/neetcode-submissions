class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # so we should use a sliding window that expands 
        # once the left pointer and the right pointer have the same chars
        # we move left once and keep going, everytime we do this, we must save the current max
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        if len(s) == 2 and s[0] != s[1]:
            return 2
        
        left,right = 0, 1
        
        res = 1
        seen = set()
        seen.add(s[0])
        while right < len(s) and left <= right:
            # print("Left val: ", s[left], " Right val: ", s[right], "Set: ", seen,"Res: ", res)
            if s[right] in seen:
                # need to move right to the next different char
                res = max(res, right - left)
                seen.remove(s[left])
                left += 1
                # need to move right to the next different char
            else:
                seen.add(s[right])
                right += 1
                res = max(res, right - left)

        return res