import os
import random

# Function to display the board
def display_board(board):
    # Clear the terminal screen (cross-platform)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-' * 5)
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-' * 5)
    print(board[1] + '|' + board[2] + '|' + board[3])

# Function to handle player input
def player_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Function to place marker on the board
def place_marker(board, marker, position):
    board[position] = marker

# Function to check for a win
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the left side
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))    # diagonal

# Function to choose which player goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Function to check if a position is available
def space_check(board, position):
    return board[position] == ' '

# Function to check if the board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Function for player to choose a position
def player_choice(board):
    position = 0
    
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

# Function to ask for replay
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# Main game logic
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
