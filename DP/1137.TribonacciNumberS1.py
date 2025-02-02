from collections import deque
class Solution:
    def tribonacci(self, n: int) -> int:
        tNums = deque([0,1,1])

        if n < 3:
            return tNums[n]

        for _ in range(n-2):
            newTnum = sum(tNums)
            tNums.append(newTnum)
            tNums.popleft()
        
        return tNums[-1]
    
# Time: O(n)
# Space: O(1)

# S#1: Iterative Solution