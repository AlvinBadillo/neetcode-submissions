class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Start by keeping only alphabetical characters and making them all lowercased
        # Array to store letters
        string = []
        # Loop through s and remove non-alphabetics
        for char in s:
            if char.isalnum():
                string.append(char.lower())
        result = ''.join(string)
        # Now initialize pointers
        i = 0
        j = len(result) - 1
        # Now compare characters of i and j and continue until they meet or until they are different
        while(i < j):
            if(result[i] != result[j]):
                return False
            i += 1
            j -= 1
        # If we made it outside the while, it means that it is a palindrome
        return True