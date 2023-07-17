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
        # verify if the movement is valid
        return 0 <= move and move <= self.n_cols and self.board[0][move] == '.'
    
    def is_terminal(self):
        # some player won the game

        # won by rows
        for row in range(self.n_rows):
            win_1  = all(self.board[row][col]==self.board[row][col+1] and not self.board[row][col] == '.' for col in range(3))
            win_2  = all(self.board[row][col]==self.board[row][col+1] and not self.board[row][col] == '.' for col in range(1, 4))
            win_3  = all(self.board[row][col]==self.board[row][col+1] and not self.board[row][col] == '.' for col in range(2, 5))
            win_4  = all(self.board[row][col]==self.board[row][col+1] and not self.board[row][col] == '.' for col in range(3, 6))
            
            if win_1 or win_2 or win_3 or win_4:
                return True
        
        # won by columns
        for col in range(self.n_cols):
            win_1 = all(self.board[row][col]==self.board[row+1][col] and not self.board[row][col] == '.' for row in range(3))
            win_2 = all(self.board[row][col]==self.board[row+1][col] and not self.board[row][col] == '.' for row in range(1, 4))
            win_3 = all(self.board[row][col]==self.board[row+1][col] and not self.board[row][col] == '.' for row in range(2, 5))

            if win_1 or win_2 or win_3:
                return True
            
        # won by up-diagonals

        for col in range(4):
            n_rows = self.n_rows-1
            diag_1 = all(self.board[n_rows-i][col+i]==self.board[n_rows-i-1][col+i+1] and not self.board[n_rows-i][col+i] == '.' 
                         for i in range(3))
            diag_2 = all(self.board[n_rows-i-1][col+i]==self.board[n_rows-i-2][col+i+1] and not self.board[n_rows-i-1][col+i] == '.' 
                         for i in range(3))
            diag_3 = all(self.board[n_rows-i-2][col+i]==self.board[n_rows-i-3][col+i+1] and not self.board[n_rows-i-2][col+i] == '.' 
                         for i in range(3))

            if diag_1 or diag_2 or diag_3:
                return True
            
        # won by down-diagonals
        for col in range(4):
            diag_1 = all(self.board[i][col+i]==self.board[i+1][col+i+1] and not self.board[i][col+i] == '.' for i in range(3))
            diag_2 = all(self.board[i+1][col+i]==self.board[i+2][col+i+1] and not self.board[i+1][col+i] == '.' for i in range(3))
            diag_3 = all(self.board[i+2][col+i]==self.board[i+3][col+i+1] and not self.board[i+2][col+i] == '.' for i in range(3))

            if diag_1 or diag_2 or diag_3:
                return True
            
        return self.valid_moves() == []
    
    def value(self):
        return 1