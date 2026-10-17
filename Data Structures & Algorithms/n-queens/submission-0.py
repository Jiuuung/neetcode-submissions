class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        #n개의 퀸이므로 무조건 가로 한칸마다 1개씩, 세로 1칸마다 1개씩 넣어야함.
        #그중에서도 대각선으로 겹치는걸 빼는것임
        queens=[]
        def change():
            sol=[]
            for (k,i) in queens:
                sol.append("."*i +"Q"+"."*(n-i-1))
            res.append(sol.copy())
            return

        def dfs(cols,remain):
            if remain==0:
                change()
                return
            for i in range(n):
                if i not in cols:
                    skip=False
                    for a,b in queens:
                        if abs(n-remain-a)==abs(b-i):
                            skip=True
                        if skip:
                            break
                    if not skip:
                        cols.add(i)
                        queens.append((n-remain,i))
                        dfs(cols,remain-1)
                        queens.pop()
                        cols.remove(i)
            return
        dfs(set({}),n)
        #좌표를 리스트 변환 함수
        return res