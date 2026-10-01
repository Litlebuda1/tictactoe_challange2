# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

# Function to get player names
def get_player_names():
    player_names = {"X": "Spieler 1", "O": "Spieler 2"}
    for marker, name in player_names.items():
        player_names[marker] = input(f"Enter the name of {name}: ")
    return player_names


# Function to create  the game board
def create_board():
    return [[str(i * 3 + j + 1) for j in range(3)] for i in range(3)]


def display_board(board):
    print("Current Board:")
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)



# Function to make a move on the board
def make_move(board, position, marker):
    row = (position - 1) // 3
    col = (position - 1) % 3
    board[row][col] = marker


def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def check_draw(board):
    for row in board:
        for cell in row:
            if cell not in ['X', 'O']:
                return False
    return True


# ... write as many functions as you need


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
player_names = get_player_names()
print(player_names)
board = create_board()
display_board(board)
print("Game setup complete. Ready to play!")
print("Player 1 is 'X' and Player 2 is 'O'.")
print("Player 1 goes first.")

print("To place your mark, enter the number corresponding" \
" to the position on the board.")


for i in range(9):
    marker = "X" if i % 2 == 1 else "O"      
    position = int(input("Enter the position for your move: "))
    make_move(board, position, marker)
    display_board(board)

    winner = check_winner(board)
    if winner:
        print(f"Herzlichen Glückwunsch! {player_names[winner]} gewinnt!")
        break

if check_winner(board) is None and check_draw(board):
    print("Unentschieden!")