class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        block_set=[(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        move_set=[(0,0),(0,1), (0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        for row in board:
            empty = row.count(".")
            row_set= set(row)
            row_set.discard(".")
            if (9-empty)!=(len(row_set)): return False
        board=[list(x) for x in zip(*board)]
        for column in board:
            empty = column.count(".")
            column_set= set(column)
            column_set.discard(".")
            if (9-empty)!=(len(column_set)): return False
       
        for block_x,block_y in block_set:
            empty=0
            tmp_set=set()
            for move_x,move_y in move_set:
                tmp=board[move_x+block_x][block_y+move_y]
                if(tmp=="."): empty+=1
                else: tmp_set.add(tmp)
            if (9-empty)!=(len(tmp_set)): return False
        return True
