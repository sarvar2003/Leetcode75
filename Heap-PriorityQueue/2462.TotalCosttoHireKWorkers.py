import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        leftCosts, rightCosts = [], []
        left, right = 0, len(costs)-1

        totalCost = 0
        while k:
            while len(leftCosts) < candidates and left <= right:
                heapq.heappush(leftCosts, costs[left])
                left += 1
            while len(rightCosts) < candidates and left <= right:
                heapq.heappush(rightCosts, costs[right])
                right -= 1 
                    
            c1 = leftCosts[0] if leftCosts else float('inf')
            c2 = rightCosts[0] if rightCosts else float('inf')

            if c1 <= c2:
                totalCost += heapq.heappop(leftCosts)
                if left <= right:
                    heapq.heappush(leftCosts, costs[left])
                    left += 1
            else:
                totalCost += heapq.heappop(rightCosts)
                if right >= left:
                    heapq.heappush(rightCosts, costs[right])
                    right -= 1
            k -= 1
            
        return totalCost

# Time: O(k*log(c))
# Space: O(c+k)

# c - candidates