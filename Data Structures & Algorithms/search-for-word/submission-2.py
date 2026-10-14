class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction=[(0,1),(1,0), (-1,0), (0,-1)]
        visited=[[False]*len(board[0]) for _ in range(len(board))]
        def dfs(y,x,index):
            if board[y][x]!=word[index]:
                return False
            if index==len(word)-1:
                return True
            
            visited[y][x]=True
            for (dy, dx) in direction:
                next_y, next_x=y+dy, x+dx
                if 0<=next_y<len(board) and 0<=next_x<len(board[0]):
                    if not visited[next_y][next_x]:
                        if dfs(next_y, next_x, index+1):
                            visited[y][x]=False
                            return True
            visited[y][x]=False
            return False
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x]==word[0]:
                    if dfs(y,x,0):
                        return True
        return False
