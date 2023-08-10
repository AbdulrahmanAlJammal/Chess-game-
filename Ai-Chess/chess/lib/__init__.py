"""
In this file, we import all the useful functions for chess from the
respective modules. Some functions that need utility of other functions from various other modules
are defined here.
"""

from chess.lib.core import (
    getType,
    isOccupied,
    isChecked,
    isEnd,
    isValidMove,
    availableMoves,
    makeMove,
)
from chess.lib.gui import (
    pygame,
    CHESS,
    drawBoard,
    drawPieces,
    prompt,
    start,
)
from chess.lib.utils import (
    initBoardVars,
    undo,
)
from chess.lib.ai import miniMax
from tools import colors
from tools.loader import BACK


# This is a gui function that draws green squares marking the legal moves of
# a seleced piece.
def showAvailMoves(win, side, board, pos, flags):
    piece = pos + [getType(side, board, pos)]
    for i in availableMoves(side, board, piece, flags):
        x = i[0] * 50 + 20
        y = i[1] * 50 + 20
        pygame.draw.rect(win, colors.GREEN, (x, y, 10, 10))


# This function makes a gentle animation of a piece that is getting moved.
# This function needs to be called BEFORE the actual move takes place
def animate(win, side, board, fro, to):

    piece = CHESS.PIECES[side][getType(side, board, fro)]
    x1, y1 = fro[0] * 50, fro[1] * 50
    x2, y2 = to[0] * 50, to[1] * 50

    stepx = (x2 - x1) / 50
    stepy = (y2 - y1) / 50

    col = colors.ORANGE if (fro[0] + fro[1]) % 2 else colors.GREY2

    clk = pygame.time.Clock()
    for i in range(51):
        clk.tick_busy_loop(100)
        drawBoard(win)
        drawPieces(win, board)
        pygame.draw.rect(win, col, (x1, y1, 50, 50))
        win.blit(piece, (x1 + (i * stepx), y1 + (i * stepy)))
        pygame.display.update()


# This is a compilation of all gui functions. This handles the display of the
# screen when chess gameplay takes place. This tool needs to be called
# everytime in the game loop.

def showScreen(win, side, board, flags, pos, player):

    drawBoard(win)

    # Back button.
    win.blit(BACK, (455, 0))

    # Turn text.
    win.blit(CHESS.TURN[int(side == player)], (10, 460))

    # Undo Button.
    win.blit(CHESS.UNDO, (10, 12))

    # Display result of the game.
    if isEnd(side, board, flags):
        if isChecked(side, board):
            win.blit(CHESS.CHECKMATE, (100, 12))
            win.blit(CHESS.LOST, (320, 12))
            win.blit(CHESS.PIECES[side]["k"], (270, 0))
        else:
            win.blit(CHESS.STALEMATE, (160, 12))
    else:

        # King check text.
        if isChecked(side, board):
            win.blit(CHESS.CHECK, (200, 12))

        # Highlights a piece's square when you click on an allied piece during your turn.
        if isOccupied(side, board, pos) and side == player:
            x = pos[0] * 50
            y = pos[1] * 50
            pygame.draw.rect(win, colors.YELLOW, (x, y, 50, 50))

    drawPieces(win, board)
    if side == player:
        showAvailMoves(win, side, board, pos, flags)

    pygame.display.update()
