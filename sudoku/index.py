def find_next_empty(puzzle):
    # Open spaces is -1
    # Return row, col tuple or (None,None)
    for row in range(9):
        for col in range(9):
            if(puzzle[row][col] ==-1):
                return row,col
    return None, None

def is_valid(puzzle, guess, row, col):
    # Row match?
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # Col match?
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Chunk vals?
    col_start = (col // 3) * 3
    row_start = (row // 3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    return True
        
def solve_sudoku(puzzle):
    # Step 1: choose somewhere to start
    row, col = find_next_empty(puzzle)

    # Not a single spot free? If so, it finish the job!
    if row is None:
        return True
    
    for guess in range(1,10):
        # Check if is a valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        puzzle[row][col] = -1
    
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)


