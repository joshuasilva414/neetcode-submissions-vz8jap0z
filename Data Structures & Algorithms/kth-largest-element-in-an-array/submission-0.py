class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush_max(heap, num)

        return heapq.nlargest(k, heap)[-1]