class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Declare hashmap
        hash = {}
        # Iterate nums and count each numbers instances
        for num in nums:
            # If num is in the hashmap, add one to the value
            if num in hash:
                hash[num] += 1
            # If not, add it
            else:
                hash[num] = 1
        # Now return the biggest k numbers in the list
        # Sort the hash values
        sortedList = sorted(hash, key=hash.get, reverse=True)
        # Filter only the top k
        result = [] 
        for i in range(k):
            result.append(sortedList[i])
        # Retrun result
        return result