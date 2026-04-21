class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h -> hours to eat each banana
        # piles[i] -> number of bananas in that spot
        # k ?
        # problem lets me know that the worst case scenerio is max(piles)
        # usign binary search instead
        R = max(piles)
        L = 1
        # add a check leter for checking worst case
        res = R
        # set up some sort of loop to try each number
        while L <= R:
            mid = (R + L) // 2
            # store how many hours it will take at each point and then add them
            total_hours = 0
            for i in range(len(piles)):
                bannanas = piles[i]
                total_hours += bannanas // mid
                # Check if i need to add one more (remainder)
                if bannanas % mid != 0:
                    total_hours += 1
            
            # now see if its a viable solution
            if total_hours <= h:
                # we have a viable solution
                res = mid
                R = mid - 1
            else:
                # if we did not meet the criteria, we are done
                L = mid + 1
        return res


# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         # h -> hours to eat each banana
#         # piles[i] -> number of bananas in that spot
#         # k ?
#         piles.sort()
#         # problem lets me know that the worst case scenerio is max(piles)
#         # brute force approach would be to try max(piles) - 1, then -2 till we find an invalid number
#         # lets code that up
#         res = max(piles)

#         temp_res = res - 1
#         # set up some sort of loop to try each number
#         while temp_res > 1:
#             # store how many hours it will take at each point and then add them
#             # dont need to store them, can count them as we go?
#             total_hours = 0
#             for i in range(len(piles)):
#                 bannanas = piles[i]
#                 total_hours += bannanas // temp_res
#                 # Check if i need to add one more (remainder)
#                 if bannanas % temp_res != 0:
#                     total_hours += 1
            
#             # now see if its a viable solution
#             if total_hours <= h:
#                 # we have a viable solution
#                 res = temp_res
#             else:
#                 # if we did not meet the criteria, we are done
#                 return res
#             temp_res -= 1
#         return res