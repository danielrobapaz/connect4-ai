import random

class connect_4():
    def __init__(self):
        # tablero 6 x 7
        self.n_rows = 6
        self.n_cols = 7
        row = ['.' for i in range(self.n_cols)]
        self.board = [row.copy() for i in range(self.n_rows)]

    def print_board(self):
        for i in range(self.n_rows,):
            print(self.board[i])
        print()

    def make_move(self, player, move):
        """
            add a token in col 'move' of the color 'player'
        """
        assert self.is_valid_move(move), 'Invalid move'
        assert player in ['R', 'Y'], 'Invalid player' 
              
        # find the las row with '0'
        last_0 = 0
        while (last_0 < self.n_rows and self.board[last_0][move] == '.'):
            last_0 += 1

        last_0 -= 1

        game_moved = connect_4()
        game_moved.board = self.board.copy()
        game_moved.board[last_0][move] = player

        return game_moved
    
    def valid_moves(self):
        return [i for i in range(self.n_cols) if self.is_valid_move(i)]

    def get_random_valid_mode(self):
        possible_moves = self.valid_moves()
        return possible_moves[random.randint(0, len(possible_moves)-1)]
    
    def is_valid_move(self, move):
        # se verifica si el movimiento es valido
        return 0 <= move and move <= self.n_cols and self.board[0][move] == '.'
    