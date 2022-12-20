class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        num_rooms = len(rooms)
        visited_rooms = set([0])
        key_queue = [] + rooms[0]
        while len(key_queue) > 0:
            curRoom = key_queue.pop()
            # print(key_queue, curRoom)

            if curRoom in visited_rooms: continue
            visited_rooms.add(curRoom)
            key_queue += rooms[curRoom]
        return num_rooms == len(visited_rooms)