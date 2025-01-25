from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        rotten_oranges = set()
        fresh_oranges = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_oranges.add((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        if not fresh_oranges: return 0
        elif not rotten_oranges: return -1

        visited = set()
        minutes = 0
        while rotten_oranges and fresh_oranges > 0:
            temp = set()
            for i, j in rotten_oranges:
                if (i,j) in visited:
                    continue
                visited.add((i,j))

                if i+1 < m and grid[i+1][j] and (i+1, j) not in visited and (i+1, j) not in temp and (i+1, j) not in rotten_oranges: 
                    temp.add((i+1,j))
                    fresh_oranges -= 1
                if j+1 < n and grid[i][j+1] and (i, j+1) not in visited and (i, j+1) not in temp and (i, j+1) not in rotten_oranges: 
                    temp.add((i,j+1))
                    fresh_oranges -= 1
                if i-1 >= 0 and grid[i-1][j] and (i-1, j) not in visited and (i-1, j) not in temp and (i-1, j) not in rotten_oranges: 
                    temp.add((i-1,j))
                    fresh_oranges -= 1
                if j-1 >= 0 and grid[i][j-1] and (i, j-1) not in visited and (i, j-1) not in temp and (i, j-1) not in rotten_oranges: 
                    temp.add((i,j-1))
                    fresh_oranges -= 1
            minutes += 1
            rotten_oranges = temp

        return -1 if fresh_oranges > 0 else minutes

# Time: O(m*n)
# Space: O(m*n)