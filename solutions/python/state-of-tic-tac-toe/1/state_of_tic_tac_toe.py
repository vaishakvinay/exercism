"""Tic-Tac-Toe game state evaluator."""


def gamestate(board):
    """Return the current state of a Tic-Tac-Toe board."""


    if len(board) != 3:
        raise ValueError("Invalid board")

    for row in board:
        if len(row) != 3:
            raise ValueError("Invalid board")
        for cell in row:
            if cell not in ("X", "O", " "):
                raise ValueError("Invalid board")

 
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)


    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")

    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

 
    x_wins = False
    o_wins = False

    for row in board:
        if row == "XXX":
            x_wins = True
        if row == "OOO":
            o_wins = True


    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            x_wins = True
        if all(board[row][col] == "O" for row in range(3)):
            o_wins = True

  
    if all(board[i][i] == "X" for i in range(3)):
        x_wins = True
    if all(board[i][i] == "O" for i in range(3)):
        o_wins = True

    if all(board[i][2 - i] == "X" for i in range(3)):
        x_wins = True
    if all(board[i][2 - i] == "O" for i in range(3)):
        o_wins = True

    if x_wins and o_wins:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if x_wins and x_count != o_count + 1:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if o_wins and x_count != o_count:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if x_wins or o_wins:
        return "win"

    if any(" " in row for row in board):
        return "ongoing"

    return "draw"   