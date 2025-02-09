class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0]*(n+1) for _ in range(m+1)]
        
        def dp(row: int, col: int) -> int:
            if row == m-1 and col == n-1:
                return 1
            if memo[row][col]:
                return memo[row][col]
            
            if row >= m or col >= n:
                return 0

            memo[row][col] = dp(row+1, col) + dp(row, col+1)

            return memo[row][col]
        
        return dp(0, 0)

# Time: O(m*n)
# Space: O(m*n)

# Top-down approach