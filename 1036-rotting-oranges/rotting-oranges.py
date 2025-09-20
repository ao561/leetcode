class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        fresh = 0
        time = 0

        def addFruit(r, c):
            nonlocal fresh
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r,c) in visit):
                return
            visit.add((r,c))
            q.append([r,c])
            fresh -= 1


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                addFruit(r+1, c)
                addFruit(r-1, c)
                addFruit(r, c+1)
                addFruit(r, c-1)
            
            time += 1
        
        return time if fresh == 0 else -1
