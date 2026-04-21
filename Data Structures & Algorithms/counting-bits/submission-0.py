class Solution:
    def countBits(self, n: int) -> List[int]:
# Declare array with base case 0
        arr = [0]
        # Iterate from 1 to n
        for i in range(1, n + 1):
            # If its a odd number, bits = 1 + bits in i/2
            if i % 2 == 1:
                arr.append(1 + arr[i//2])
            # If its even, bits = bits in i/2
            else:
                arr.append(arr[i//2])
        return arr
        
        