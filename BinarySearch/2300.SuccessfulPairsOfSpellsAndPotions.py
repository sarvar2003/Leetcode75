import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)

        def binarySearch(target: int) -> int:
            if target > potions[-1]:
                return n
            high, low = n, 0

            while high >= low:
                mid = low + (high - low) // 2

                if potions[mid] >= target:
                    high = mid-1
                else:
                    low = mid+1

            return mid if potions[mid] == target else low

        res = []
        for s in spells:
            num = math.ceil(success/s)
            ind = binarySearch(num)

            res.append(n-ind)
            
        return res

# Time: O(n*log(n))
# Space: O(m)

# n - len(potions)
# m - len(spells)