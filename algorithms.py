"""
    Implementation of the negamax algorithms. There are two versions implemented.
    The classical negamax and the alpha beta pruning version
"""
import math

def negamax(game, depth, player):
    if player == 'R':
        color = 1
        new_player = 'Y'
    else:
        color = -1
        new_player = 'R'

    if ((depth == 0) or game.is_terminal()):
        return color * game.value()

    alpha = -math.inf
    possibles_moves = game.valid_moves()    

    for move in possibles_moves:
        child = game.make_move(player, move)

        old_alpha = alpha
        alpha = max(alpha, -negamax(child, depth-1, new_player))

        if alpha != old_alpha:
            game.best_move = move        
    return game.best_move

def negamax_alpha_beta(game, depth, alpha, beta, player):
    if player == 'R':
        color = 1
        new_player = 'Y'
    else:
        color = -1
        new_player = 'R'

    if ((depth == 0) or game.is_terminal()):
        return color * game.value()

    possible_moves = game.valid_moves()
    score = -math.inf

    for move in possible_moves:
        child = game.make_move(player, move)
        value = -negamax_alpha_beta(child, depth-1, -beta, -alpha, new_player)

        old_score = score
        score = max(score, value)
        alpha = max(alpha, value)

        if score != old_score:
            game.best_move = move
        
        if (alpha >= beta): break

    return game.best_move