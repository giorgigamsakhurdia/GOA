def check_tic_tac_toe(board):
    n = len(board)  # დაფის ზომა (n x n)

    # ამოწმებს რიგებს და სვეტებს
    for i in range(n):
        if all(cell == "X" for cell in board[i]):
            return "X"
        if all(cell == "O" for cell in board[i]):
            return "O"
        if all(board[j][i] == "X" for j in range(n)):
            return "X"
        if all(board[j][i] == "O" for j in range(n)):
            return "O"

    # ამოწმებს მთავარ დიაგონალს
    if all(board[i][i] == "X" for i in range(n)):
        return "X"
    if all(board[i][i] == "O" for i in range(n)):
        return "O"

    # ამოწმებს გვერდით დიაგონალს
    if all(board[i][n - i - 1] == "X" for i in range(n)):
        return "X"
    if all(board[i][n - i - 1] == "O" for i in range(n)):
        return "O"

    # ამოწმებს ფრე ან განგრძობს თამაშს
    if any("" in row for row in board):
        return "Game not finished"

    return "Draw"

# მაგალითი გამოყენებისთვის
board = [
    ["X", "O", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"]
]

result = check_tic_tac_toe(board)
print(result)  # "Draw"
