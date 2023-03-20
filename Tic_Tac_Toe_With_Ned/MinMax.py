Ned, Human = '1', '-1'

def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '0'):
                return True
    return False

def evaluate(b):
    # Checking for Rows for X or O victory.
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == Ned):
                return 10
            elif (b[row][0] == Human):
                return -10

    # Checking for Columns for X or O victory.
    for col in range(3):

        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):

            if (b[0][col] == Ned):
                return 10
            elif (b[0][col] == Human):
                return -10

    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

        if (b[0][0] == Ned):
            return 10
        elif (b[0][0] == Human):
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

        if (b[0][2] == Ned):
            return 10
        elif (b[0][2] == Human):
            return -10
    return 0

def minimax(board, depth, isMax):
    score = evaluate(board)
    if (score == 10):
        return score

    if (score == -10):
        return score

    if (isMovesLeft(board) == False):
        return 0

    if (isMax):
        best = -1000

        for i in range(3):
            for j in range(3):

                if (board[i][j] == '0'):
                    board[i][j] = Ned

                    best = max(best, minimax(board,
                                             depth + 1,
                                             not isMax))

                    board[i][j] = '0'
        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):

                if (board[i][j] == '0'):
                    board[i][j] = Human

                    best = min(best, minimax(board, depth + 1, not isMax))

                    board[i][j] = '0'
        return best

def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):

            if (board[i][j] == '0'):

                board[i][j] = Ned

                moveVal = minimax(board, 0, False)

                board[i][j] = '0'

                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove

