class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys, visited = set(), {}
        keys.add(0)

        while keys and len(visited) < len(rooms):
            curRoom = keys.pop()
            
            if curRoom in visited:
                continue
            visited[curRoom] = True
            
            for key in rooms[curRoom]:
                keys.add(key)

        return len(visited) == len(rooms)

# Time: O(n)
# Space: O(n)