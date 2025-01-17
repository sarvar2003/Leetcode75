from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        cost = {}

        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append(b)
            graph[b].append(a)
            cost[(a, b)] = values[i]
            cost[(b, a)] = 1/values[i]

        res, stack = [], []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1)
                continue

            stack.append([start, 1])
            visited = set()

            found = False
            while stack:
                curr_var, curr_val  = stack.pop()

                if curr_var in visited: continue
                visited.add(curr_var)

                if curr_var == end:
                    res.append(curr_val)
                    found = True
                    break
                
                for next_var in graph[curr_var]:
                    if next_var not in visited:
                        stack.append([next_var, curr_val*cost[(curr_var, next_var)]])
            
            if not found:
                res.append(-1)
                

        return res

# Time: O(N*(V+E)) : N - number of queries
# Space: O(V+E)