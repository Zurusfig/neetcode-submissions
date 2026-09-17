class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        grid_check = {0:set(), 1:set(),2:set(),3:set(),4:set(),5:set(),6:set(),7:set(),8:set()}
        
        for i in range(9):
            row_check = set()
            col_check = set()
            for j in range(9):
                cell1 = board[i][j]
                if cell1 in row_check:
                    return False
                elif cell1 != ".":
                    row_check.add(cell1)
                cell2 = board[j][i]
                if cell2 in col_check:
                    return False
                elif cell2 != ".":
                    col_check.add(cell2)

                grid = 8
                if i < 3:
                    if j < 3:
                        grid = 0
                    elif j < 6:
                        grid = 1
                    else:
                        grid = 2
                elif i < 6:
                    if j < 3:
                        grid = 3
                    elif j < 6:
                        grid = 4
                    else:
                        grid = 5
                else:
                    if j < 3:
                        grid = 6
                    elif j < 6:
                        grid = 7
                
                if cell1 in grid_check[grid]:
                    return False
                elif cell1 != ".":
                    grid_check[grid].add(cell1)
        
        return True
