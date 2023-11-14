import collections
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Most optimized solution, time complexity: O(n), space: O(n)
        # Bucket sort, with an array size = len(nums)
        # index is the frequency, value is the list of number appeared for that frequency
        # Pop k elements from that array to retrieve most frequent k elements

        bucketArray = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for key, value in count.items():
            bucketArray[value].append(key)
        
        result = []
        for i in range(len(bucketArray) - 1, 0, -1):
            for n in bucketArray[i]:
                result.append(n)
                if len(result) == k:
                    return result
    
    def topKFrequentWithHeap(self, nums: list[int], k: int) -> list[int]:
        # Use heap to get k most frequent element O(klogn)
        # Build heap O(n), get value from heap O(log K)
        count = {}
        for n in nums:
            count[n] = 1 + count.get(nums[n], 0)
        
        maxHeap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(maxHeap) # O(n) to heapify a list with n items
        result = []
        while k > 0:
            result.append(heapq.heappop(maxHeap)[1]) # each pop take log(n) and we do that k time so k*log(n)
        return result