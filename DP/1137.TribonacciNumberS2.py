class Solution:
    def tribonacci(self, n: int) -> int:

        def dp(n: int, memo: List[int]) -> int:
            if memo[n] != -1:
                return memo[n]
            
            if n == 0:
                res = 0
            elif n == 1 or n == 2:
                res = 1
            else:
                res = dp(n-1, memo) + dp(n-2, memo) + dp(n-3, memo)

            memo[n] = res
            return res

        memo = [-1] * (n+1)
        return dp(n, memo)

# Time: O(n)
# Space: O(n)

# S#2: Recursive Solution