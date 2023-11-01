import random


def clear_output():
    print("\n" * 100)


def init_game():
    board_value = [
        "#",  # filler for board_value[0]
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ]

    return board_value


def player_turn(board_value, playernum, marker):
    # Player chooses a slot, display board after
    print(f"Player {playernum} :")
    display_board(place_marker(board_value, marker))

    # Check board for winning pattern of tie.
    game_status = win_check(board_value, playernum, marker)
    # print(game_status)
    return game_status


def play_again():
    restartgame = ""
    while (restartgame != "Y") or (restartgame != "N"):
        restartgame = input("Do you want to play again? (Y or N) : ").upper()
        if restartgame == "Y":
            return True
        elif restartgame == "N":
            return False


def display_board(board):
    clear_output()

    # Print board status
    print("Here is the current tic-tac-toe board:")
    print("----------------------------")
    print(f"|   {board[1]}    |   {board[2]}    |   {board[3]}    |")
    print("----------------------------")
    print(f"|   {board[4]}    |   {board[5]}    |   {board[6]}    |")
    print("----------------------------")
    print(f"|   {board[7]}    |   {board[8]}    |   {board[9]}    |")
    print("----------------------------")


def choose_marker():
    """
    Player chooses what marker to use. Return assigned marker per player
    and the order.
    """
    marker = ""
    playernum = random.randint(1, 2)  # randomize who will go first

    print(f"Player order has been randomized, player {playernum} will go first")

    # Check if player 1 will use X or O. If input is not this 2, ask again.
    while not (marker == "X" or marker == "O"):
        marker = input(f"What marker will player {playernum} use? (X or O): ").upper()

    if (marker == "X" and playernum == 1) or (marker == "O" and playernum == 2):
        return ("X", "O", playernum)  # player 1 = X, player2 = O
    elif (marker == "X" and playernum == 2) or (marker == "O" and playernum == 1):
        return ("O", "X", playernum)  # player 1 = O, player2 = X


def place_marker(board_value, marker):
    """
    Ask player input and check if it's a number and if it's between 1:9
    """
    choice = "not valid"
    within_range = False

    # Check if player input is a digit and if within 1-9
    while choice.isdigit() == False or within_range == False:
        choice = input("Choose an available number of the board (1-9): ")

        # If entered value is not a digit, ask again.
        if choice.isdigit() == False:
            print("Invalid entry. Pick again")

        # If entered value is a digit and is still available in the current board.
        if (
            choice.isdigit() == True
            and int(choice) in range(1, 10)
            and board_value[int(choice)] == " "  # Check if slot is still available
        ):
            within_range = True
            board_value[
                int(choice)
            ] = marker  # replace board value with player's marker
        else:
            within_range = False

    return board_value


def win_check(board_value, playernum, marker):
    # if board is same with any winning combination, end game
    if (
        (
            # across the bottom
            board_value[7] == marker
            and board_value[8] == marker
            and board_value[9] == marker
        )
        or (
            # across the middle
            board_value[4] == marker
            and board_value[5] == marker
            and board_value[6] == marker
        )
        or (
            # across the top
            board_value[1] == marker
            and board_value[2] == marker
            and board_value[3] == marker
        )
        or (
            # left vertical
            board_value[7] == marker
            and board_value[4] == marker
            and board_value[1] == marker
        )
        or (
            # middle vertical
            board_value[8] == marker
            and board_value[5] == marker
            and board_value[2] == marker
        )
        or (
            # right vertical
            board_value[9] == marker
            and board_value[6] == marker
            and board_value[3] == marker
        )
        or (
            # diagonal left to right
            board_value[1] == marker
            and board_value[5] == marker
            and board_value[9] == marker
        )
        or (
            # diagonal right to left
            board_value[3] == marker
            and board_value[5] == marker
            and board_value[7] == marker
        )
    ):
        print(f"Player {playernum} WINS!")
        return "end"

    # if board is full, end game
    elif " " not in board_value:
        print("It's a TIE!")
        return "end"

    # if no win or tie status, just continue game.
    else:
        return "ongoing"


############# Main game ################
# List for debugging
testboard_value = ["#", "X", "O", "X", "O", "X", "O", "X", "O", "O"]

# Initial blank board and game status.
board_value = init_game()
game_status = "start"

# While there are still slots available, continue the game.
while " " in board_value:
    # Initialization of blank board, player order and player marker at start of game.
    if game_status == "start":
        # Initial board is blank
        board_value = init_game()

        # Show Initial Board with all blank
        display_board(board_value)

        # Assign Marker for player 1 and player 2; Output is a tuple
        (player1_marker, player2_marker, first_player) = choose_marker()
        game_status = "ongoing"  # ongoing

    # Player 1 first
    if first_player == 1:
        # Player 1's turn
        game_status = player_turn(board_value, 1, player1_marker)

        # Check if they want to play again after "end"
        if game_status == "end":
            if play_again():
                game_status = "start"
                board_value = init_game()
                continue
            else:
                print("Game Over!!")
                break  # end game
        # Do nothing if no end game condition satisfied yet
        elif game_status == "ongoing":
            pass

        # Player 2's turn
        game_status = player_turn(board_value, 2, player2_marker)

        # Check if they want to play again after "end"
        if game_status == "end":
            if play_again():
                game_status = "start"
                board_value = init_game()
                continue
            else:
                print("Game Over!!")
                break  # end game
        # Do nothing if no end game condition satisfied yet
        elif game_status == "ongoing":
            pass

    # Player 2 first
    elif first_player == 2:
        # Player 2's turn
        game_status = player_turn(board_value, 2, player2_marker)
        # Check if they want to play again after "end"
        if game_status == "end":
            if play_again():
                game_status = "start"
                board_value = init_game()
                continue
            else:
                print("Game Over!!")
                break  # end game
        # Do nothing if no end game condition satisfied yet
        elif game_status == "ongoing":
            pass

        # Player 1's turn
        game_status = player_turn(board_value, 1, player1_marker)
        # Check if they want to play again after "end"
        if game_status == "end":
            if play_again():
                game_status = "start"
                board_value = init_game()
                continue
            else:
                print("Game Over!!")
                break  # end game
        # Do nothing if no end game condition satisfied yet
        elif game_status == "ongoing":
            pass
