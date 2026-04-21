class Solution:
    def reverseBits(self, n: int) -> int:
        # Transform number to binary representation
        # Then invert it
        # Then convert it to decimal

        # Transform input to binary and remove leading 0b
        binary_input = str(bin(n))[2:].zfill(32)
        print(binary_input)
        # Reverse binary representation of input
        reversed_b_input = "".join(reversed(binary_input))
        print(reversed_b_input)

        reversed_decimal = int(reversed_b_input, 2)
        return reversed_decimal
        