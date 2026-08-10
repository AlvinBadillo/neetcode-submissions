class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for letter in s:
            if letter in my_dict:
                my_dict[letter] += 1
            else:
                my_dict[letter] = 1
        print(my_dict)

        my_dict2 = {}
        for letter in t:
            print(letter)
            if letter in my_dict2:
                my_dict2[letter] += 1
            else:
                my_dict2[letter] = 1

        return my_dict == my_dict2


