from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = set([(a,b) for a, b in connections])
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append(b) 
            graph[b].append(a)


        visited = set()
        changes = 0
        cities = [0]

        while cities:
            city = cities.pop()
            
            if city in visited: continue
            visited.add(city)

            for neighbor in graph[city]:
                if neighbor in visited: continue
                if (neighbor, city) not in edges:
                    changes += 1
                cities.append(neighbor)
        
        return changes


# Time: O(V+E)
# Space: O(V+E)