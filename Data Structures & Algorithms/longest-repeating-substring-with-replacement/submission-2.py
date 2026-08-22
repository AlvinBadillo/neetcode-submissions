class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = { 
            "A": 0, 
            "B": 0, 
            "C": 0, 
            "D": 0, 
            "E": 0, 
            "F": 0, 
            "G": 0, 
            "H": 0, 
            "I": 0,
            "J": 0,
            "K": 0,
            "L": 0,
            "M": 0,
            "N": 0,
            "O": 0,
            "P": 0,
            "Q": 0,
            "R": 0,
            "S": 0,
            "T": 0,
            "U": 0,
            "V": 0,
            "W": 0,
            "X": 0,
            "Y": 0,
            "Z": 0
        }

        # we have a max window size of # of the max repeated character in the window + k
        # If the len of our window is greater than that then we dont have a valid window
        left, right = 0, 1
        if len(s) == 0:
            return 0
        res = 1
        seen[s[0]] += 1

        while right < len(s):
            seen[s[right]] += 1
            # if current window not valid, we have to shrink it
            while (right - left + 1) > max(seen.values()) + k: 
                seen[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res