# Define the board as a list of 9 spaces
board = [' ' for _ in range(9)]

def print_board():
    """Prints the current state of the board."""
    rows = [f"|{board[i]}|{board[i+1]}|{board[i+2]}|" for i in range(0, 9, 3)]
    print("\n" + "\n".join(rows) + "\n")

def empty_squares():
    """Returns True if there are empty squares on the board."""
    return ' ' in board

def num_empty_squares():
    """Returns the number of empty squares on the board."""
    return board.count(' ')

def make_move(square, letter):
    """Places the given letter ('X' or 'O') on the board at the specified square."""
    board[square] = letter

def undo_move(square):
    """Removes the letter from the board at the specified square."""
    board[square] = ' '

def winning(letter):
    """Checks if the given letter ('X' or 'O') has won the game."""
    win_conditions = [
        [0, 1, 2],  # Horizontal wins
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # Vertical wins
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # Diagonal wins
        [2, 4, 6]
    ]
    for condition in win_conditions:
        if all(board[i] == letter for i in condition):
            return True
    return False

def minimax(depth, alpha, beta, maximizing_player):
    """The Minimax algorithm with alpha-beta pruning to find the optimal move."""
    if winning('O'):
        return {'score': 10 - depth}
    elif winning('X'):
        return {'score': depth - 10}
    elif not empty_squares():
        return {'score': 0}

    if maximizing_player:
        best_move = {'score': -float('inf')}
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                result = minimax(depth + 1, alpha, beta, False)
                board[i] = ' '
                result['index'] = i
                if result['score'] > best_move['score']:
                    best_move = result
                alpha = max(alpha, best_move['score'])
                if beta <= alpha:
                    break
        return best_move
    else:
        best_move = {'score': float('inf')}
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                result = minimax(depth + 1, alpha, beta, True)
                board[i] = ' '
                result['index'] = i
                if result['score'] < best_move['score']:
                    best_move = result
                beta = min(beta, best_move['score'])
                if beta <= alpha:
                    break
        return best_move

def player_move():
    """Prompts the player to make a move and updates the board."""
    while True:
        try:
            move = int(input('Enter your move (0-8): '))
            if 0 <= move < 9 and board[move] == ' ':
                make_move(move, 'X')
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")

def main():
    """Main function to run the Tic-Tac-Toe game."""
    while empty_squares():
        print_board()

        if num_empty_squares() % 2 == 1:
            # Player's turn
            player_move()
        else:
            # AI's turn
            move = minimax(0, -float('inf'), float('inf'), True)['index']
            make_move(move, 'O')

        if winning('O'):
            print_board()
            print('You Lose!')
            break
        elif winning('X'):
            print_board()
            print('You Won!')
            break
        elif not empty_squares():
            print_board()
            print('Game Tie.')
            break
if _name_ == "_main_":
    main()