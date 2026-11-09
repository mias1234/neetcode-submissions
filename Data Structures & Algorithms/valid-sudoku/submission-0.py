class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            box = 0
            row = 0
            col = 0
            for j in range(9):
                row_cell_val = board[i][j]
                if row_cell_val != ".":
                    mask = 1 << int(row_cell_val)
                    if row & mask:
                        return False
                    row |= mask
                
                col_cell_val = board[j][i]
                if col_cell_val != ".":
                    mask = 1 << int(col_cell_val)
                    if col & mask:
                        return False
                    col |= mask
                
                box_cell_val = board[(i//3)*3+(j//3)][(i%3)*3+(j%3)]
                if box_cell_val != ".":
                    mask = 1 << int(box_cell_val)
                    if box & mask:
                        return False
                    box |= mask
        return True

