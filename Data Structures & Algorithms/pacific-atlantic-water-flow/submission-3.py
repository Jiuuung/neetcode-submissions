class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        direction = [(0,1), (1,0),(0,-1), (-1,0)]
        visited=[[0b00]*col for _ in range(row)]
        q=deque()
        for i in range(col):
            visited[0][i]=0b10
            visited[row-1][i]=0b01
            q.append((0,i))
            q.append((row-1,i))
        for i in range(row):
            visited[i][0]|=0b10
            visited[i][col-1]|=0b01
            q.append((i,0))
            q.append((i,col-1))
        if col!=1 or row!=1:
            out=[[0,col-1],[row-1,0]]
        else:
            out=[[0,0]]
            return out
        while q:
            r,c=q.popleft()
            vi=visited[r][c]
            h=heights[r][c]
            for dr, dc in direction:
                nr, nc=r+dr, c+dc
                if 0<=nr<row and 0<=nc<col and heights[nr][nc]>=h and (vi&~visited[nr][nc])!=0:
                    visited[nr][nc]|=vi
                    q.append((nr,nc))
                    if visited[nr][nc]==0b11:
                        out.append([nr,nc])
        return out


        


