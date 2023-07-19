"""
    Proyecto 4 CI5437 - Inteligencia Artifical 1
    Connect 4
"""

import connect4
import algorithms
import time

if __name__ == '__main__':

    ("(0) Negamax; (1) Negamax with alpha-beta pruning: ")
    chosen_algorithm = input("(0) Negamax; (1) Negamax with alpha-beta pruning.\
                             \nInsert a number to pick one of the algorithms: ")

    print(f'You chose {chosen_algorithm}.\n')

    game = connect4.connect_4()
    computer_player = 'R'
    human_player = 'Y'

    while not game.is_terminal():
        print("X\'s turn!")
        print("Wait while the computer thinks its move!\n")

        if chosen_algorithm == '0':
            move_to_make = algorithms.negamax(game, 6, computer_player)
        elif chosen_algorithm == '1':
            move_to_make = algorithms.negamax_alpha_beta(game, 8, -200, 200, computer_player)

        game = game.make_move(computer_player, move_to_make)
        game.print_board()

        if game.is_terminal():
            print('End! The computer has won!')
            break

        move_to_make = int(input(f'Y\'s turn!\nChoose a column to move to = {game.valid_moves()}: '))
        game = game.make_move(human_player, move_to_make)
        print()
        game.print_board()

        if game.is_terminal():
            print('End! You have won!')
            break