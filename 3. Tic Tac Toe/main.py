x = '❌ '
o = '⭕ '
Playing = False
columns_dict = {
    'A': 0, 
    'B': 1, 
    'C': 2,
    }


def empty_board():
    spaces = [['   ', '   ', '   '], ['   ', '   ', '   '], ['   ', '   ', '   ']]
    return spaces

def start_up():
    start_up = input("Want to play Tic Tac Toe? (Y/N): ").upper()
    if start_up == "Y":
        return True
    elif start_up == "N":
        print("Okay, see ya!")
        return False
    else:
        print("Invalid input - try again!")
        start_up()


def choose_symbol():
    player_choice = input("Do you want to be ❌ or ⭕?: ").upper()
    if player_choice == "X":
        print(f"Player 1 is {x} and Player 2 is {o}")
        return x, o 
    elif player_choice == "O":
        print(f"Player 1 is {o} and Player 2 is {x}")
        return o, x
    else:
        print("Invalid input - try again.")
        choose_symbol()


def make_board(spaces):
    board = f"""
              A   B   C

        1    {spaces[0][0]}┃{spaces[0][1]}┃{spaces[0][2]}
             ━━━ ━━━ ━━━
        2    {spaces[1][0]}┃{spaces[1][1]}┃{spaces[1][2]}
             ━━━ ━━━ ━━━
        3    {spaces[2][0]}┃{spaces[2][1]}┃{spaces[2][2]}
        """
    print(board)


def make_move(symbol, spaces):
    move_row = input(f"{symbol} player, where do you want to go? First select the row (1, 2, or 3): ")
    if move_row not in ('1', '2', '3'):
        print("Invalid input - try again.")
        make_move(symbol)
    move_column = input("Now select the column (A, B, or C): ").upper()
    if move_column not in ('A', 'B', 'C'):
        print("Invalid input - start the move over.")
        make_move(symbol)
    if spaces[int(move_row) - 1][columns_dict[move_column]] == '   ':
        spaces[int(move_row) - 1][columns_dict[move_column]] = symbol
    else:
        print("Can't go there! Start the move over.")
        make_move(symbol)


def check_board(spaces):
    if spaces[0][0] == spaces[0][1] and spaces[0][0] == spaces[0][2] and spaces[0][0] != '   ':
        print(f"{spaces[0][0]}wins!")
        return False
    elif spaces[1][0] == spaces[1][1] and spaces[1][0] == spaces[1][2] and spaces[1][0] != '   ':
        print(f"{spaces[1][0]}wins!")
        return False
    elif spaces[2][0] == spaces[2][1] and spaces[2][0] == spaces[2][2] and spaces[2][0] != '   ':
        print(f"{spaces[2][0]}wins!")
        return False
    elif spaces[0][0] == spaces[1][0] and spaces[0][0] == spaces[2][0] and spaces[0][0] != '   ':
        print(f"{spaces[0][0]}wins!")
        return 
    elif spaces[0][1] == spaces[1][1] and spaces[0][1] == spaces[2][1] and spaces[0][1] != '   ':
        print(f"{spaces[0][1]}wins!")
        return False
    elif spaces[0][2] == spaces[1][2] and spaces[0][2] == spaces[2][2] and spaces[0][2] != '   ':
        print(f"{spaces[0][2]}wins!")
        return False
    elif spaces[0][0] == spaces[1][1] and spaces[0][0] == spaces[2][2] and spaces[0][0] != '   ':
        print(f"{spaces[0][0]}wins!")
        return False
    elif spaces[0][2] == spaces[1][1] and spaces[0][2] == spaces[2][0] and spaces[0][2] != '   ':
        print(f"{spaces[0][2]}wins!")
        return False
    elif not any('   ' in sublist for sublist in spaces):
        print("Tie!")
        return False
    else:
        return True

def play_game():
    if start_up():
        spaces = empty_board()
        symbols = choose_symbol()
        player1 = symbols[0]
        player2 = symbols[1]
        make_board(spaces)
        Playing = True
    else:
        return
    while Playing:
        make_move(player1, spaces)
        make_board(spaces)
        if not check_board(spaces):
            break
        make_move(player2, spaces)
        make_board(spaces)
        if not check_board(spaces):
            break
    play_game()

play_game()
