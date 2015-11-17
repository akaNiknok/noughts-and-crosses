"""Noughts and Crosses
Popularly known as Tic-Tac-Toe
"""

import random


def main():
    
    # Create board
    board = []
    for x in range(3):
        board.append([" "] * 3)

    # Decide who will be the first to play
    if random.randint(0, 1) == 0:
        turn = "PLAYER"
        player_sym = "X"
        comp_symbol = "O"
    else:
        turn = "COMPUTER"
        player_sym = "O"
        comp_symbol = "X"

    # Main Loop
    while check_winner(board) == False:
        print_board(board)
        print("{}'s turn".format(turn))

        # Get player's move
        if turn == "PLAYER":
            while True:
                player_x = int(input("X = "))
                player_y = int(input("Y = "))

                # Check if player's move is valid
                if ((player_x <= 2 and player_x >= 0) and
                    (player_y <= 2 and player_y >= 0)):
                    if board[player_y][player_x] == " ":
                        board[player_y][player_x] = player_sym
                        turn = "COMPUTER"
                        break

        else:
            pass
            #TODO: Artificial Intellignece

    print_board(board)
    # Print the winner
    if check_winner(board) == player_sym:
        print("YOU WON!!! :-)")  # YEHEY!!!
    else:
        print("You Lost :-(")  # :-P


def print_board(board):
    """Prints the board"""
    
    print
    print("  0   1   2")
    for i in range(3):
        print("{} {} | {} | {}").format(i, *board[i])
        if i != 2:
            print(" ---+---+---")
    print("============")


def check_winner(board):
    """Returns the winner else False if there is no winner"""

    # Check Horizontals
    if board[0][0] == board[0][1] == board[0][2] != " ":
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] != " ":
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] != " ":
        return board[2][0]

    # Check Verticals
    elif board[0][0] == board[1][0] == board[2][0] != " ":
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] != " ":
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] != " ":
        return board[0][2]

    # Check Diagonals
    elif board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    elif board[2][0] == board[1][1] == board[0][2] != " ":
        return board[2][0]

    else:
        return False


def find_danger(board):
    """Returns the coord of the danger spot else False if nothing found"""
    pass


main()