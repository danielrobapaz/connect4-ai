"""
    Proyecto 4 CI5437 - Inteligencia Artifical 1
    Connect 4
"""

import connect4
import algorithms
import time

if __name__ == '__main__':
    game = connect4.connect_4()
    
    player = 'R'

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