class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)
        res = -1
        while k:
            res = - heapq.heappop(maxHeap)
            k -= 1
        return res