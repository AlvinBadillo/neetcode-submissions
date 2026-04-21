class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Set up both pointers and result variable
        i = 0
        j = len(heights) - 1
        result = 0
        # Set up loop
        while(i < j):
            # Calculate current area
            curr = (j - i) * min(heights[i], heights[j])
            # Now compare curr with result and keep the largest
            result = max(result, curr)
            # Now its time to figure out which index to move
            # I should always move the smaller of the two
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return result