import connect4
import math
import sys

def negamax(connect4, depth, player):

    connect4.print_board()

    if player == 'R':
        color = 1
        new_player = 'Y'
    else:
        color = -1
        new_player = 'R'
    
    if ((depth == 0) or connect4.is_terminal()):
        return color * connect4.value()
    
    alpha = -math.inf
    moves_queue = connect4.valid_moves()

    if len(moves_queue) == 0:
        alpha = -negamax(connect4, depth, new_player)

    while len(moves_queue) > 0:
        child = moves_queue[0]
        moves_queue.pop(0)

        alpha = max(alpha, -negamax(connect4.make_move(player, child),
                                    depth-1, new_player))
    return alpha


def negamax_alpha_beta(connect4, depth, alpha, beta, player):

    connect4.print_board()

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

    if len(moves_queue) == 0:
        score = -negamax_alpha_beta(connect4, depth, -beta, -alpha, new_player)

    while len(moves_queue) > 0:

        child = moves_queue[0]
        moves_queue.pop(0)

        value = -negamax_alpha_beta(connect4.make_move(player, child),
                                    depth-1, -beta, -alpha, new_player)
        score = max(score, value)
        alpha = max(alpha, value)

        if (alpha >= beta): break

    return score


def negascout(connect4, depth, alpha, beta, color):
    if ((depth == 0) or connect4.is_terminal()):
        return color * connect4.value()
    
    moves_queue = connect4.valid_moves(color)
    curr_player = color == 1
    n_moves = moves_queue.size()

    if (moves_queue.empty()):
        return -negascout(connect4, depth, -beta, -alpha, -color)
    
    for i in range(n_moves):
        child = moves_queue[0]
        moves_queue.pop(0)

        if i == 0:
            score = -negascout(connect4.make_move(curr_player, child),
                               depth -1, -beta, -alpha, -color)
        else:

            score = -negascout(connect4.make_move(curr_player, child),
                               depth -1, -alpha - 1, -alpha, -color)
            
            if (alpha < score and score < beta):
                score = -negascout(connect4.make_move(curr_player, child),
                                   depth -1, -beta, -score, -color)
        
        alpha = max(alpha, score)

        if (alpha >= beta): break

    return alpha

def test(connect4, depth, color, score, condition):
    if ((depth == 0) or connect4.is_terminal()):
        connect4.value() > score
        if connect4.value() >= score:
            result = True
        return result

    moves_queue = connect4.valid_moves(color)
    curr_player = color == 1
    n_moves = moves_queue.size()

    if (moves_queue.empty()):
        if (curr_player and test(connect4, depth, -color, score, condition)):
            return True
        if (not curr_player and not test(connect4, depth, -color, score, condition)):
            return False
        
    for i in range(n_moves):
        child = moves_queue[0]
        moves_queue.pop(0)

        if (curr_player and test(connect4.make_move(curr_player, child),
                                 depth - 1, -color, score, condition)):
            return True
        
        if (not curr_player and not test(connect4.make_move(curr_player, child),
                                         depth -1, -color, score, condition)):
            return False
        
    return not curr_player

def scout(connect4, depth, color):
    if (depth == 0 or connect4.is_terminal()):
        return color * connect4.value()
    
    moves_queue = connect4.valid_moves(color)
    curr_player = color == 1
    n_moves = moves_queue.size()

    score =  -200

    if (moves_queue.empty()):
        return scout(connect4, depth, -color)
    
    for i in range(n_moves):
        child = moves_queue[0]
        moves_queue.pop(0)

        value = scout(connect4.make_move(curr_player, child), depth -1, -color)

        if i == 0:
            score = value
        else:
            if (curr_player and test(connect4.make_move(curr_player, child),
                                     depth-1, -color, score, False)):
                score = value
            elif (not curr_player and not test(connect4.make_move(curr_player, child),
                                               depth-1, -color, score, True)):
                score = value

    return score