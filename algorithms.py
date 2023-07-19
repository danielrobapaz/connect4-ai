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

def negamax_alpha_beta(connect4, depth, alpha, beta, player):
    if player == 'R':
        color = 1
        new_player = 'Y'
    else:
        color = -1
        new_player = 'R'

    if ((depth == 0) or connect4.is_terminal()):
        return color * connect4.value()

    moves_queue = connect4.valid_moves()
    score = -math.inf

    while len(moves_queue) > 0:

        child = moves_queue[0]
        moves_queue.pop(0)

        value = -negamax_alpha_beta(connect4.make_move(player, child),
                                    depth-1, -beta, -alpha, new_player)
        score = max(score, value)
        alpha = max(alpha, value)

        if (alpha >= beta): break

    return score