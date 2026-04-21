class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                # Use a dictionary, key -> number, value -> frequency
        my_dict = dict()

        # Iterate nums and store data in nums
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        # Now I want to find the k bigest values among the list of values of the dict
        # I want to keep the key of that value
        sorted_pairs = sorted(my_dict.items(), key = lambda x: x[1], reverse=True)
        # Now iterate sorted_pairs k times and create a new list to store x[0]
        result = []
        for i in range(k):
            result.append(sorted_pairs[i][0])
        return result