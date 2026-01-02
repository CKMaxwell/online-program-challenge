# 20200911 - Tic Tac Toe
def tic_tac_toe(board):
    ans = "Draw"
    for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                if board[i][0] == "O":
                    ans = "O"
                if board[i][0] == "X":
                    ans = "X"
                break
    for j in range(3):
            if board[0][j] == board[1][j] == board[2][j]:
                if board[0][j] == "O":
                    ans = "O"
                if board[0][j] == "X":
                    ans = "X"
                break
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "O":
            ans = "O"
        if board[0][0] == "X":
            ans = "X"
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "O":
            ans = "O"
        if board[0][2] == "X":
            ans = "X"
    return ans

print(tic_tac_toe([
  ["X", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]))