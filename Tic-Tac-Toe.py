import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a winning combination
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(row[i] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'X'):
        return 1
    elif is_winner(board, 'O'):
        return -1
    elif len(get_empty_cells(board)) == 0:
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, False)
            board[i][j] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, True)
            board[i][j] = ' '
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 'X'
        score = minimax(board, 0, False)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_over = False

    while not game_over:
        print_board(board)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue
        board[row][col] = 'O'

        if is_winner(board, 'O'):
            print_board(board)
            print("You win!")
            break
        elif len(get_empty_cells(board)) == 0:
            print_board(board)
            print("It's a tie!")
            break

        best_move = get_best_move(board)
        board[best_move[0]][best_move[1]] = 'X'

        if is_winner(board, 'X'):
            print_board(board)
            print("AI wins!")
            break
        elif len(get_empty_cells(board)) == 0:
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()

