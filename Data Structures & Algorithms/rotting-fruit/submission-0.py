class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q=deque()
        fresh=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        minute=0
        while q and fresh>0:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in direction:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        q.append((nr,nc))
                        fresh-=1
            minute+=1
        
        return minute if fresh==0 else -1