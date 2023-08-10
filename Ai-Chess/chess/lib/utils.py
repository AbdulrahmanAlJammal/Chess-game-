"""
In this file, we define a few other non-gui My-PyChess helper functions.
"""


from chess.lib.core import makeMove


# Return the initial state (in which a chess game starts) of the chess variables
# side, board and flags

def initBoardVars():
    side = False
    board = [
        [
            [1, 7, "p"], [2, 7, "p"], [3, 7, "p"], [4, 7, "p"],
            [5, 7, "p"], [6, 7, "p"], [7, 7, "p"], [8, 7, "p"],
            [1, 8, "r"], [2, 8, "n"], [3, 8, "b"], [4, 8, "q"],
            [5, 8, "k"], [6, 8, "b"], [7, 8, "n"], [8, 8, "r"],
        ], [
            [1, 2, "p"], [2, 2, "p"], [3, 2, "p"], [4, 2, "p"],
            [5, 2, "p"], [6, 2, "p"], [7, 2, "p"], [8, 2, "p"],
            [1, 1, "r"], [2, 1, "n"], [3, 1, "b"], [4, 1, "q"],
            [5, 1, "k"], [6, 1, "b"], [7, 1, "n"], [8, 1, "r"],
        ]
    ]
    flags = [[True for _ in range(4)], None]
    return side, board, flags


# Undo your last move. (Re-do all moves from the start up until your last move.)

def undo(moves):
    side, board, flags = initBoardVars()
    moves = moves[:-2]
    for fro, to in moves:
        side, board, flags = makeMove(side, board, fro, to, flags)
    return side, board, flags, moves
