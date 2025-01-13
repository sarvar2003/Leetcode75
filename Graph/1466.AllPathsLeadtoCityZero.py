from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        connectionsToZero = set([0])
        changes = 0
        
        stack = connections.copy()
        while stack and len(connectionsToZero) <= len(connections):
            temp = []
            for a, b in stack:
                if not b or b in connectionsToZero:
                    connectionsToZero.add(a)
                elif not a or a in connectionsToZero:
                    changes += 1
                    connectionsToZero.add(b)
                else:
                    temp.append([a,b])
            stack = temp
                
        return changes

# Time: O(n^2)
# Space: O(n)