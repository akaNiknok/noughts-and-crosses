"""Noughts and Crosses
Popularly known as Tic-Tac-Toe
"""

import random
import os
import time


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
    while check_winner(board) == False and board_filled(board) == False:
        print_board(board)
        print("{}'s turn".format(turn))

        # Get player's move
        if turn == "PLAYER":
            while True:
                try:
                    player_x = int(input("X = "))
                except (NameError, ValueError):
                    print("Please enter a number")
                    continue
                try:
                    player_y = int(input("Y = "))
                except (NameError, ValueError):
                    print("Please enter a number")
                    continue

                # Check if player's move is valid
                if ((player_x <= 2 and player_x >= 0) and
                    (player_y <= 2 and player_y >= 0)):
                    if board[player_y][player_x] == " ":
                        board[player_y][player_x] = player_sym
                        turn = "COMPUTER"
                        break
                    else:
                        print("The coordinates you entered is not valid")
                else:
                    print("Please enter a number from 0-2")

        # Get computer's move
        else:
            danger = find_danger_score(board)  # Check if player is about to score

            # If player is about to score, block him
            if danger != False:
                board[danger[0]][danger[1]] = comp_symbol
                turn = "PLAYER"

            # Else put it anywhere ;-)
            else:
                while True:
                    comp_x = random.randint(0, 2)
                    comp_y = random.randint(0, 2)

                    # Check if move is valid
                    if board[comp_y][comp_x] == " ":
                        board[comp_y][comp_x] = comp_symbol
                        turn = "PLAYER"
                        break

            # Makes the computer look like it is thinking like a human being :)
            print("Wait... I'm thinking... -_-")
            time.sleep(random.randint(2,5))

    print_board(board)
    # Print the winner
    if check_winner(board) == player_sym:
        print("YOU WON!!! :-)")  # YEHEY!!!
    elif check_winner(board) == comp_symbol:
        print("You Lost :-(")    # :-P
    else:
        print("It's a DRAW!!!")  # -_-


def print_board(board):
    """Prints the board"""
    
    os.system("clear")
    print("  0   1   2 X")
    for i in range(3):
        print(("{} {} | {} | {}").format(i, *board[i]))
        if i != 2:
            print(" ---+---+---")

    print("Y")
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

def board_filled(board):
    """Checks if the board is already filled"""

    # Check if there is an empty box in board
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                return False

    return True

def find_danger_score(board):
    """Returns the coord of the danger/score spot else False if none found"""
    
    # Find danger/score spot in Horizontals
    for row in range(3):
        if ((board[row].count("X") == 2 and board[row].count(" ") == 1) or
            (board[row].count("O") == 2 and board[row].count(" ") == 1)):
            return row, board[row].index(" ")

    # Find danger/score spot in Columns
    for col in range(3):
        if ((list(zip(*board))[col].count("X") == 2 and
            list(zip(*board))[col].count(" ") == 1) or
            (list(zip(*board))[col].count("O") == 2 and
             list(zip(*board))[col].count(" ") == 1)):
            return list(zip(*board))[col].index(" "), col

    # Initialize list for diagonals `\` & `/`
    diagonals = [
        [board[0][0], board[1][1], board[2][2]],  # `\`
        [board[2][0], board[1][1], board[0][2]]   # `/`
    ]

    # Find danger/score spot in Diagonals
    for diagonal in range(2):
        if ((diagonals[diagonal].count("X") == 2 and
            diagonals[diagonal].count(" ") == 1) or
            (diagonals[diagonal].count("O") == 2 and
            diagonals[diagonal].count(" ") == 1)):

            # Get the index of blank spot
            index = diagonals[diagonal].index(" ")

            # If the index of the blank spot is in the `\`, just return the
            # same index since its x and y coordinates are ALWAYS the same
            if diagonal == 0:
                return index, index
            else:
                if index == 0:
                    return 2, 0
                elif index == 1:
                    return 1, 1
                else:
                    return 0, 2

    return False


main()