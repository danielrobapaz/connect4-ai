import connect4
import sys

expanded = 0
generated = 0

def negamax(connect4, depth, color):
    
    if connect4.is_terminal():
        expanded += 1
        return color * connect4.value()
    
    alpha, child = -float('inf')
    curr_player = color == 1

    moves_queue = connect4.valid_moves(color)

    if (moves_queue.empty()):
        generated += 1
        alpha = -negamax(connect4, depth, -color)

    while len(moves_queue) > 0:
        generated += 1
        moves_queue.pop(0)

        child = moves_queue[0]
        alpha = max(alpha, -negamax(connect4.make_move(curr_player, child),
                                    depth-1, -color))


def negamax_alpha_beta(connect4, depth, alpha, beta, color):
    if ((depth == 0) or connect4.is_terminal()):
        expanded += 1
        return color * connect4.value()

    moves_queue = connect4.valid_moves(color)
    score = -sys.maxint - 1
    curr_player = color == 1

    if (moves_queue.empty()):
        generated += 1
        score = -negamax_alpha_beta(connect4, depth, -beta, -alpha, -color)

    while (len(moves_queue) > 0):
        generated += 1

        child = moves_queue[0]
        moves_queue.pop(0)

        value = -negamax_alpha_beta(connect4.make_move(curr_player, child),
                                    depth-1, -beta, -alpha, -color)
        score = max(score, value)
        alpha = max(alpha, value)

        if (alpha >= beta): break

    return score


def negascout(connect4, depth, alpha, beta, color):
    if ((depth == 0) or connect4.is_terminal()):
        expanded += 1
        return color * connect4.value()
    
    moves_queue = connect4.valid_moves(color)
    curr_player = color == 1
    n_moves = moves_queue.size()

    if (moves_queue.empty()):
        return -negascout(connect4, depth, -beta, -alpha, -color)
    
    for i in range(n_moves):
        generated += 1
        child = moves_queue[0]
        moves_queue.pop(0)

        if i == 0:
            score = -negascout(connect4.make_move(curr_player, child),
                               depth -1, -beta, -alpha, -color)
        else:
            generated += 1
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
        return (condition ? connect4.value() >= score : connect4.value() > score)
        # Acomodar esto

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
        expanded += 1
        return color * connect4.value()
    
    moves_queue = connect4.valid_moves(color)
    curr_player = color == 1
    n_moves = moves_queue.size()

    score =  -200

    if (moves_queue.empty()):
        generated += 1
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