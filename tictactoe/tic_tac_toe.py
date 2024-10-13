import math

def print_board(board):
    """Prints the current state of the board."""
    print("\n")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(f" {row} ")
        if i < 2:
            print("---+---+---")
    print("\n")

def is_winner(board, player):
    """Checks if the specified player has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]              
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return all(cell != ' ' for cell in board)

def get_available_moves(board):
    """Returns a list of available moves."""
    return [i for i, cell in enumerate(board) if cell == ' ']

def minimax(board, depth, is_maximizing, ai_player, human_player):
    """Minimax algorithm implementation."""
    if is_winner(board, ai_player):
        return 10 - depth
    if is_winner(board, human_player):
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = ai_player
            score = minimax(board, depth + 1, False, ai_player, human_player)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = human_player
            score = minimax(board, depth + 1, True, ai_player, human_player)
            board[move] = ' '
            best_score = min(score, best_score)
        return best_score

def ai_move(board, ai_player, human_player):
    """Determines the best move for the AI."""
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = ai_player
        score = minimax(board, 0, False, ai_player, human_player)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def human_move(board, human_player):
    """Prompts the human player to make a move."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move not in range(9):
                print("Invalid move. Please enter a number between 1 and 9.")
            elif board[move] != ' ':
                print("Cell already taken. Choose another one.")
            else:
                board[move] = human_player
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def main():
    board = [' ' for _ in range(9)]
    human_player = ''
    ai_player = ''

    
    while human_player not in ['X', 'O']:
        human_player = input("Do you want to be X or O? ").upper()
        if human_player not in ['X', 'O']:
            print("Invalid choice. Please choose X or O.")
    ai_player = 'O' if human_player == 'X' else 'X'

    
    turn = ''
    while turn not in ['Y', 'N']:
        turn = input("Do you want to go first? (Y/N): ").upper()
        if turn not in ['Y', 'N']:
            print("Invalid choice. Please enter Y or N.")

    game_over = False
    print_board(board)

    while not game_over:
        if turn == 'Y':
            
            human_move(board, human_player)
            print_board(board)
            if is_winner(board, human_player):
                print("Congratulations! You win!")
                game_over = True
                continue
            turn = 'N'
        else:
            
            print("AI is making a move...")
            move = ai_move(board, ai_player, human_player)
            board[move] = ai_player
            print_board(board)
            if is_winner(board, ai_player):
                print("AI wins! Better luck next time.")
                game_over = True
                continue
            turn = 'Y'

        if is_board_full(board):
            print("It's a draw!")
            game_over = True

if __name__ == "__main__":
    main()
    