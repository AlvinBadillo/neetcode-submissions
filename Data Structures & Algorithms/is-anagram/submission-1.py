class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
                # Use hashmap to keep count of ocurrences of each letter
        my_hash = dict()

        # Iterate s and add for every instance
        for char in s:
            if char not in my_hash:
                my_hash[char] = 1
            else:
                my_hash[char] += 1
        # Iterate t and substract for every instance
        for char in t:
            if char not in my_hash:
                return False
            else:
                my_hash[char] -= 1
                if my_hash[char] < 0: return False
        return all(value == 0 for value in my_hash.values())