class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        col, row = len(grid[0]), len(grid)
        inf=2147483647
        q=deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    q.append((i,j))
        direction=[(0,-1), (0,1), (1,0),(-1,0)]
        while q:
            r,c= q.popleft()
            for dr, dc in direction:
                nr, nc= r+dr, c+dc
                if 0<=nr<row and 0<=nc<col and grid[nr][nc]==inf:
                    grid[nr][nc]=grid[r][c]+1
                    q.append((nr,nc))
        return