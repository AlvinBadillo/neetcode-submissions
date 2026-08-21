class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        res = []
        def two_sum(target, nums_2):
            left, right = 0, len(nums_2)-1
            while left < right:
                l = nums_2[left]
                r = nums_2[right]
                combination = target + l + r
                if combination == 0:
                    res.append([target, l, r])
                    while left + 1 < len(nums_2) and nums_2[left] == nums_2[left + 1]:
                        left += 1
                    else:
                        left += 1
                    while right - 1 > 0 and nums_2[right] == nums_2[right - 1]:
                        right -= 1
                    else:
                        right -= 1
                elif combination > 0:
                    right -= 1
                else:
                    left += 1

        seen = set()
        # so we want to check each entry against the rest of the list
        for i in range(len(nums_sorted)):
            target = nums_sorted[i]
            if target in seen:
                continue
            seen.add(target)
            entry = two_sum(target, nums_sorted[i+1:])
            if entry:
                res.append(entry)
        return res

