class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(num):
            if len(sol) == k:
                if sum(sol) == n:
                    res.append(sol[:])
                return
            
            if num > 9:
                return
            
            backtrack(num+1)
            sol.append(num)
            backtrack(num+1)
            sol.pop()
        
        backtrack(1)
        
        return res

# Time: O(1) 
# Space: O(1)

# Constant because the time complexity is not related to n or k its O(2^9) all the time
# and space is O(9) every time