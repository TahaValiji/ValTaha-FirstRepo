board = [" - ", " - ", " - ",
         " - ", " - ", " - ", 
         " - ", " - ", " - "]

game_running = True
winner = None
current_player = " X "

def play_game():
    name = input("What is the name for X's place player: ").title()
    name2 = input("What is the name for O's place player: ").title()
    print(f"Welcome {name} and {name2} to the game :)")

    display_board()
    while game_running:
        turns(current_player)
        check_game_over()
        flip_player()

        if winner == " X ":
            print(f"{name} won!")
        elif winner == " O ":
            print(f"{name2} won!")
        elif winner == None:
            print("Tie!")

def check_rows():
    global game_running

    row1 = board[0] == board[1] == board[2] != " - "
    row2 = board[3] == board[4] == board[5] != " - "
    row3 = board[6] == board[7] == board[8] != " - "

    if row1 or row2 or row3:
        game_running = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return None

def check_columns():
    global game_running

    column1 = board[0] == board[3] == board[6] != " - "
    column2 = board[1] == board[4] == board[7] != " - "
    column3 = board[2] == board[5] == board[8] != " - "

    if column1 or column2 or column3:
        game_running = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return None

def check_diagonals():
    global game_running

    diagonal1 = board[0] == board[4] == board[8] != " - "
    diagonal2 = board[6] == board[4] == board[2] != " - "

    if diagonal1 or diagonal2:
        game_running = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    return None

def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2], " 1 | 2 | 3 ")
    print(board[3] + '|' + board[4] + '|' + board[5], " 4 | 5 | 6 ")
    print(board[6] + '|' + board[7] + '|' + board[8], " 7 | 8 | 9 ")

def check_game_over():
    check_winner()
    check_tie()

def check_winner():
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    
def check_tie():
    global game_running

    if " - " not in board:
        game_running = False
        return True
    return False

def turns(player):
    print(f"{player}'s turns")
    position = input("Enter your choice from number 1 to 9: ")

    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Enter your choice from number 1 to 9: ")
            
        position = int(position) - 1

        if board[position] == " - ":
            valid = True
        else:
            print("Sorry! You can't choose that position, Try again.")

        board[position] = player
        display_board()

def flip_player():
    global current_player

    if current_player == " X ":
        current_player = " O " 
    elif current_player == " O ":
        current_player = " X "
    
ask = input("Hey! Do you want to play Tic-Tac-Toe (Yes or No): ").lower()
if ask == 'yes':
    play_game()
else:
    exit()