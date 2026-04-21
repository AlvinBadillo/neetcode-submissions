class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Empty dictionary, key = number, value = index in list
        seen = dict()
        # Loop through nums
        for i in range(len(nums)):
            # See if we have a number in the dictionary whose sum with num is the target
            want = target - nums[i]
            if want in seen:
                minIndex = min(seen[want], i)
                maxIndex = max(seen[want], i)
                return [minIndex, maxIndex]
            # If I havent found a match for num, add it to the dictionary
            # If its the firsy entry no problem, if there is already an entry, dont add it
            if nums[i] not in seen:
                seen[nums[i]] = i
        