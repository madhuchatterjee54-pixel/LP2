# Simple N-Queen Program using Backtracking

# Number of queens / size of chessboard
N = 4


# Function to print the chessboard solution
# 1 represents queen placed
# 0 represents empty space

def print_board(board):

    print("Solution is:\n")

    # Traverse every row
    for i in range(N):

        # Traverse every column
        for j in range(N):

            # Print current cell value
            print(board[i][j], end=" ")

        # Move to next line after one row is printed
        print()


# Function to check whether queen can be placed safely
# We check:
# 1. Left side row
# 2. Upper left diagonal
# 3. Lower left diagonal

def is_safe(board, row, col):

    # Check left side of current row
    for i in range(col):

        # If queen already exists in same row
        if board[row][i] == 1:
            return False


    # Check upper-left diagonal
    i = row
    j = col

    while i >= 0 and j >= 0:

        # If queen found
        if board[i][j] == 1:
            return False

        # Move diagonally upward-left
        i = i - 1
        j = j - 1


    # Check lower-left diagonal
    i = row
    j = col

    while i < N and j >= 0:

        # If queen found
        if board[i][j] == 1:
            return False

        # Move diagonally downward-left
        i = i + 1
        j = j - 1


    # Position is safe
    return True


# Recursive function to solve N-Queen problem

def solve_nq(board, col):

    # Base case
    # If all queens are placed
    if col >= N:
        return True


    # Try placing queen in every row
    for i in range(N):

        # Check whether current position is safe
        if is_safe(board, i, col):

            # Place queen
            board[i][col] = 1


            # Recursively place next queen
            if solve_nq(board, col + 1):
                return True


            # BACKTRACKING STEP
            # Remove queen if solution not found
            board[i][col] = 0


    # If queen cannot be placed
    return False


# Main Function

def main():

    # Create empty chessboard
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]


    # Call recursive function
    if solve_nq(board, 0) == False:

        print("Solution does not exist")

    else:

        # Print solution
        print_board(board)


# Function Calling
main()
