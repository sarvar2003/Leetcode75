import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pop_cnt = len(nums) - k
        heapq.heapify(nums)
        
        for _ in range(pop_cnt):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)

# Time: O(n)
# Space:O(1)