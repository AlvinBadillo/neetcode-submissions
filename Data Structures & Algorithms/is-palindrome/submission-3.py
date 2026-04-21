class Solution:
    def isPalindrome(self, s: str) -> bool:
        # First remove everuthing that is not a letter
        filtered_s = []
        for item in s:
            if item.isalnum():
                filtered_s.append(item.lower())

        # Now set up two pointers
        # Left at 0 and Right at len(filtered_s)
        left = 0
        right = len(filtered_s) - 1
        # Now I will check if left is equal to right
        # If it is, move left to the right and right to the left and keep going
        # However, if left is not equal to right,we can instanly return false
        # Because they are different and will no longer be considered as a palindrome
        while(left < right):
            if filtered_s[left] != filtered_s[right]:
                return False
            else:
                left += 1
                right -= 1
        # If we exit the loop it means we found a pailindrome so we can return True
        return True