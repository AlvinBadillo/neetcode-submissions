class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row, col = 0, 0
        # verify rows
        for row in range(9):
            dups = set()
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in dups:
                        print("Found dup on rows")
                        return False
                    else:
                        dups.add(board[row][col])
        
        # Verify cols
        for col in range(9):
            dups = set()
            for row in range(9):
                if board[row][col] != '.':
                    if board[row][col] in dups:
                        print("found dup on cols")
                        print("Dup: ", board[row][col], "Set: ", dups)
                        return False
                    else:
                        dups.add(board[row][col])
        my_dict = {}
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':    
                    # Calculate where we are
                    ROW = row // 3
                    COL = col // 3
                    # First check if we have an entry from this square
                    if (ROW, COL) in my_dict:
                        # If there is, check if the current value is in the set
                        if board[row][col] in my_dict[(ROW, COL)]:
                            return False
                        else:
                            my_dict[(ROW,COL)].add(board[row][col])
                    else:
                        my_dict[(ROW,COL)] = set()
                        my_dict[(ROW,COL)].add(board[row][col])

        return True

board=[
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]]    





