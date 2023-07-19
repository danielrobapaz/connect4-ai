"""
    Proyecto 4 CI5437 - Inteligencia Artifical 1
    Connect 4
"""

import connect4
import algorithms
import time

if __name__ == '__main__':
    '''
    game = connect4.connect_4()
    
    player = 'R'

    print("Game played with random moves:")
    while not game.is_terminal():
        move_to_make = game.get_random_valid_mode()
        
        game = game.make_move(player, move_to_make)
        game.print_board()
        print(game.value())

        if player == 'R':
            player = 'Y'
        elif player == 'Y':
            player = 'R'

        time.sleep(0.5)
    '''

    #print("Game played with algorithms: ")
    game = connect4.connect_4()
    computer_player = 'R'
    human_player = 'Y'

    while not game.is_terminal():
        # Call negamax algorithm
        move_to_make = algorithms.negamax(game, 6, computer_player)
        game = game.make_move(computer_player, move_to_make)
        game.print_board()

        if game.is_terminal():
            print('End.')
            break

        move_to_make = int(input(f'Your move (\'Y\') valid moves = {game.valid_moves()}: '))
        game = game.make_move(human_player, move_to_make)
        game.print_board()