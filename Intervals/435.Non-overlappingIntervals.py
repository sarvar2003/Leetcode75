class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[0])
        currEnd = -float('inf')

        ans = 0
        for start, end in intervals:
            if start < currEnd:
                ans += 1
                end = min(currEnd, end)

            currEnd = end
        
        return ans

# Time: O(nlogn)
# Space: O(1)