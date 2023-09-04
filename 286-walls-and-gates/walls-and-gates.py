class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit or rooms[r][c] == -1:
                return
            visit.add((r, c))
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)

            dist += 1
