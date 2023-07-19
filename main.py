"""
    Proyecto 4 CI5437 - Inteligencia Artifical 1
    Connect 4
"""

import connect4
import algorithms
import time

if __name__ == '__main__':

    print("(0) Ai vs Ai; (1) Ai vs Human")
    chosen_modality = input("Insert a number to pick one of the modalities: ")

    print("\n(0) Negamax; (1) Negamax with alpha-beta pruning: ")
    chosen_algorithm = input("Insert a number to pick one of the algorithms: ")

    chosen_depth = int(input("\nInsert a number to pick the maximum depth the algorithm will go to: "))
    print()

    game = connect4.connect_4()
    computer_player = 'R'
    human_player = 'Y'

    while not game.is_terminal():
        print("R\'s turn!\n")

        if chosen_modality == '1':
            print("Wait while the computer's thinking!...\n")

        R_time_start = time.time()
        if chosen_algorithm == '0':
            move_to_make = algorithms.negamax(game, chosen_depth, computer_player)
        elif chosen_algorithm == '1':
            move_to_make = algorithms.negamax_alpha_beta(game, chosen_depth, -200, 200, computer_player)
        R_time_end = time.time()

        print(f'R\'s Thinking time: {round(R_time_end - R_time_start, 2)} seconds') 
        print(f'R\'s move: {move_to_make}\n')

        game = game.make_move(computer_player, move_to_make)
        game.print_board()

        if game.is_terminal():
            print('End! R has won!')
            break

        print("Y\'s turn!\n")

        if chosen_modality == '0':
            Y_time_start = time.time()
            if chosen_algorithm == '0':
                move_to_make = algorithms.negamax(game, chosen_depth, computer_player)
            elif chosen_algorithm == '1':
                move_to_make = algorithms.negamax_alpha_beta(game, chosen_depth, -200, 200, computer_player)
            Y_time_end = time.time()  

            print(f'Y\'s Thinking time: {round(Y_time_end - Y_time_start, 2)} seconds')
            print(f'Y\'s move: {move_to_make}\n')

        elif chosen_modality == '1':
            move_to_make = int(input(f'Choose a column to move to = {game.valid_moves()}: '))    

        game = game.make_move(human_player, move_to_make)
        print()
        game.print_board()

        if game.is_terminal():
            print('End! Y has won!')
            break