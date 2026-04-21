class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squared(num):
            # Calculate the sum of the swuares of its digits
            s = 0
            while num > 0:
                # Get first digit
                f = num % 10
                s = s + f**2
                num = num // 10
            return s
        n = sum_of_squared(n)
        # set to keep track of seen numbers
        seen = set()
        while(1):
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = sum_of_squared(n)