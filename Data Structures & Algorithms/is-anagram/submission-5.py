class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # my_dict = {}
        # for letter in s:
        #     if letter in my_dict:
        #         my_dict[letter] += 1
        #     else:
        #         my_dict[letter] = 1
        # print(my_dict)

        # my_dict2 = {}
        # for letter in t:
        #     print(letter)
        #     if letter in my_dict2:
        #         my_dict2[letter] += 1
        #     else:
        #         my_dict2[letter] = 1

        # return my_dict == my_dict2

        if len(s) != len(t):
            return False

        alphabet = [0 for i in range(26)]

        for letter in range(len(s)):
            alphabet[ord(s[letter]) - ord("a")] += 1 
            alphabet[ord(t[letter]) - ord("a")] -= 1

        for val in alphabet:
            if val != 0:
                return False
        return True 







