class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first get all the values -> ocurrances
        my_dict = {}
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        import heapq
        max_heap = []
        # this heap will have a tuple (ocurrance, number)

        for key in my_dict:
            heapq.heappush(max_heap, (-my_dict[key], key))

        res = []
        for i in range(k):
            ocurrance, num = heapq.heappop(max_heap)
            res.append(num)
        return res