# 1. Initialize the 3x3 game board (2D list)
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def display_board(b):
    """Prints the current state of the Tic-Tac-Toe board."""
    print("\n  0 1 2")
    print(" -------")
    # Loop through each row and print the contents
    for i in range(3):
        print(f"{i}| {b[i][0]} {b[i][1]} {b[i][2]}")
    print(" -------")

def check_win(b, player):
    """Checks for a win in horizontal, vertical, and diagonal lines."""
    
    # Check Horizontal wins
    for row in b:
        if all(cell == player for cell in row):
            return True
    
    # Check Vertical wins (transpose the board logic)
    for col in range(3):
        if all(b[row][col] == player for row in range(3)):
            return True
            
    # Check Diagonal wins
    # Top-Left to Bottom-Right
    if all(b[i][i] == player for i in range(3)):
        return True
    # Top-Right to Bottom-Left
    if all(b[i][2 - i] == player for i in range(3)):
        return True
        
    return False

def check_draw(b):
    """Checks if the board is full (a draw)."""
    # If there is no winner and no empty spaces (' '), it's a draw
    return all(cell != ' ' for row in b for cell in row)

def is_valid_move(b, row, col):
    """Validates the player's move: checks boundaries and if the cell is empty."""
    if 0 <= row < 3 and 0 <= col < 3 and b[row][col] == ' ':
        return True
    return False

def get_player_move(current_player):
    """Prompts the current player for a move (row and column) and validates input."""
    while True:
        try:
            # Get row input
            row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
            # Get column input
            col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))
            
            # Check if the move is valid before returning it
            if is_valid_move(board, row, col):
                return row, col
            else:
                print("Invalid move. Cell is already taken or out of bounds. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")

# Main game loop function
def play_game():
    """Runs the core Tic-Tac-Toe game logic."""
    current_player = 'X'
    game_over = False
    
    print("Welcome to Console Tic-Tac-Toe!")
    
    while not game_over:
        # 1. Display the board
        display_board(board)
        
        # 2. Get and validate the player's move
        row, col = get_player_move(current_player)
        
        # 3. Update the board
        board[row][col] = current_player
        
        # 4. Check for a win
        if check_win(board, current_player):
            display_board(board)
            print(f"\n🎉 Player {current_player} Wins! Congratulations! 🎉")
            game_over = True
        
        # 5. Check for a draw
        elif check_draw(board):
            display_board(board)
            print("\nIt's a Draw! Game Over. 🤝")
            game_over = True
            
        # 6. Switch players if the game is not over
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Start the game
if __name__ == "__main__":
    play_game()