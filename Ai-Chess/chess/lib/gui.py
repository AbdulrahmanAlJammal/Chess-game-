"""
In this file, we define some basic gui-related functions
"""
import pygame
from tools.loader import CHESS
from tools import colors


# Apply 'convert_alpha()' on all pieces to optimise images for speed.
def convertPieces(win):
    for i in range(2):
        for key, val in CHESS.PIECES[i].items():
            CHESS.PIECES[i][key] = val.convert_alpha(win)


# This function draws the board.
def drawBoard(win):
    # Board background
    win.fill(colors.MIST)

    # Board first color.
    pygame.draw.rect(win, colors.ORANGE, (50, 50, 400, 400))

    # Every other square with second color.
    for y in range(1, 9):
        for x in range(1, 9):
            if (x + y) % 2 == 0:
                pygame.draw.rect(win, colors.GREY2,
                                 (50 * x, 50 * y, 50, 50))


# This funtion draws all pieces onto the board.
def drawPieces(win, board):
    for side in range(2):
        for x, y, ptype in board[side]:
            win.blit(CHESS.PIECES[side][ptype], (x * 50, y * 50))


# This function displays the prompt screen when a user tries to quit or leave game.
# User must choose Yes or No, this function returns True or False respectively.
def prompt(win):
    # Prompt background.
    pygame.draw.rect(win, colors.BLACK, (110, 160, 280, 130))

    # Prompt border.
    pygame.draw.rect(win, colors.GOLD, (110, 160, 280, 130), 2)

    # Prompt message.
    win.blit(CHESS.MESSAGE[0], (130, 165))
    win.blit(CHESS.MESSAGE[1], (190, 195))

    # Yes/No buttons.
    win.blit(CHESS.YES, (145, 240))
    win.blit(CHESS.NO, (305, 240))

    pygame.display.flip()

    while True:

        # Get user input.
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:

                if 240 < event.pos[1] < 270:

                    # User clicked yes.
                    if 140 < event.pos[0] < 200:
                        return True

                    # User clicked no.
                    elif 300 < event.pos[0] < 350:
                        return False


# This function shows a small animation when the game starts, while also
# optimising images for display - call only once per game
def start(win):

    convertPieces(win)
    clk = pygame.time.Clock()
    for i in range(101):
        clk.tick_busy_loop(140)
        drawBoard(win)

        for j in range(8):
            win.blit(CHESS.PIECES[0]["p"], (0.5 * i * (j + 1), 225 + 1.25 * i))
            win.blit(CHESS.PIECES[1]["p"], (0.5 * i * (j + 1), 225 - 1.25 * i))

        for j, pc in enumerate(["r", "n", "b", "q", "k", "b", "n", "r"]):
            win.blit(CHESS.PIECES[0][pc], (0.5 * i * (j + 1), 225 + 1.75 * i))
            win.blit(CHESS.PIECES[1][pc], (0.5 * i * (j + 1), 225 - 1.75 * i))

        # Update screen every frame.
        pygame.display.update()
