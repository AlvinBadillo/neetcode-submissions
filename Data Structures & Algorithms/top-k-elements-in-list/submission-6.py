class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # first get all the values -> ocurrances
        # my_dict = {}
        # for num in nums:
        #     if num in my_dict:
        #         my_dict[num] += 1
        #     else:
        #         my_dict[num] = 1

        # import heapq
        # max_heap = []
        # # this heap will have a tuple (ocurrance, number)

        # for key in my_dict:
        #     heapq.heappush(max_heap, (-my_dict[key], key))

        # res = []
        # for i in range(k):
        #     ocurrance, num = heapq.heappop(max_heap)
        #     res.append(num)
        # return res

        # bucket sort
        # make a list of all posible ocurrances as its index
        # then the values of that bucket are thenumbers who have tha ammount of ocurances
        buckets = []

        for i in range(len(nums) + 1):
            buckets.append([])
        
        # now make the dict we made before
        my_dict = {}
        for i in range(len(nums)):
            curr = nums[i]
            if curr in my_dict:
                my_dict[curr] += 1
            else:
                my_dict[curr] = 1
        
        for key, value in my_dict.items():
            # print(key,value)
            buckets[value].append(key)
        # print(buckets)
        res = []
        for i in range(len(buckets)-1, 0, -1):
            curr_bucket = buckets[i]
            for n in curr_bucket:
                res.append(n)
                if len(res) == k:
                    return res
        return res





