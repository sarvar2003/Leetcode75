from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        min_steps = float('inf')
        m, n = len(maze), len(maze[0])
        queue = deque([[entrance, 0]])
        visited = set()
        min_possible = min(entrance[0], entrance[1], m-entrance[0], n-entrance[1])
        
        while queue:
            pos, steps = queue.popleft()
            row, col = pos
            
            if (row, col) in visited: continue
            visited.add((row, col))

            if ((row==0 or col==0) or (row==m-1 or  col==n-1)) and pos != entrance:
                min_steps = min(steps, min_steps)
                if min_steps <= min_possible: break
            
            if row+1 < m and maze[row+1][col] == '.':
                queue.append([[row+1,col], steps+1])

            if row-1 >= 0 and maze[row-1][col] == '.':
                queue.append([[row-1,col], steps+1])

            if col+1 < n and maze[row][col+1] == '.':
                queue.append([[row,col+1], steps+1])

            if col-1 >= 0 and maze[row][col-1] == '.':
                queue.append([[row,col-1], steps+1])

        return min_steps if min_steps < float('inf') else -1

# Time: O(M*N) 
# Space: O(M*N)

#  M - len(maze), N - len(maze[0])