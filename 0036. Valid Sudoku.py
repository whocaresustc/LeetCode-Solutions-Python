# time O(n*n), space O(n*n)
class Solution2(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        res = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    num = board[row][col]  # str, don't change to int!
                    if (row, num) in res or (num, col) in res \
                    or (num, row//3, col//3) in res:
                        return False
                    res.add((row, num))
                    res.add((num, col))
                    res.add((num, row//3, col//3))
        return True


# time O(n*n), space O(n)
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N, M = 9, 3
        
        for i in range(N):
            row = set()
            col = set()
            box = set()
            for j in range(N):
                if board[i][j] in row:  # check row i
                    return False
                elif board[i][j] != ".":
                    row.add(board[i][j])
                    
                if board[j][i] in col:  # check col i
                    return False
                elif board[j][i] != ".":
                    col.add(board[j][i])
                
                num = board[(i//M)*M+j//M][(i%M)*M+j%M]
                if num in box:  # check box i
                    return False
                elif num != ".":
                    box.add(num)
        
        return True


"""

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

"""