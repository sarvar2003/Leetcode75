class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x:x[0])
        
        res = 0
        currEnd = -float('inf')

        for start, end in points:
            
            if currEnd < start:
                res += 1
                currEnd = end
            else:
                currEnd = min(currEnd, end)

        return res

# Time: O(nlogn)
# Space: O(1)