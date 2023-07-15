"""
    possibles boards states in which any player won
"""
n_cols = 7

win_by_column = [
    # win in column i
    [[(0, i), (1, i), (2, i), (3, i)],
    [(1, i), (2, i), (3, i), (4, i)],
    [(2, i), (3, i), (4, i), (5, i)]]

    for i in range(n_cols)
]
win_by_row = []
win_by_diagonal = []