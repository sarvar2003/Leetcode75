import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        if h == n:
            return max(piles)
        
        if n == 1:
            return math.ceil(piles[0]/h)

        low, high = 1, max(piles)+1
        res = float('inf')

        while low < high:
            k = (high+low)//2
            curH = 0
            for pile in piles:
                curH += math.ceil(pile/k)
            
            if curH > h:
                low = k+1
            else:
                high = k
                res = min(res, k)

        return 

# Time: O(log(m))
# Space: O(1)

# m - max(piles)+1