"""
Loading and rendering all resources used across the project.
"""

import os.path
import pygame
from tools import colors

# Initialize pygame.font module and load the font file.
pygame.font.init()
FONT = os.path.join("res", "BebasNeue-Regular.ttf")

# Load different sizes of the font.
head = pygame.font.Font(FONT, 80)
large = pygame.font.Font(FONT, 65)
small = pygame.font.Font(FONT, 27)
vsmall = pygame.font.Font(FONT, 17)

# Loading all images needed.
BGSPRITE = pygame.image.load(os.path.join("res", "img", "bgsprites.jpg"))
PSPRITE = pygame.image.load(os.path.join("res", "img", "piecesprite.png"))
BACK = pygame.image.load(os.path.join("res", "img", "bk1.png"))
ICON = pygame.image.load(os.path.join("res", "img", "icon.gif"))
SELECT = pygame.image.load(os.path.join("res", "img", "select.jpg"))


# Game resources

class CHESS:
    # Render all the pieces.
    PIECES = ({}, {})
    for i, ptype in enumerate(["k", "q", "b", "n", "r", "p"]):
        for side in range(2):
            PIECES[side][ptype] = PSPRITE.subsurface(
                (i * 50, side * 50, 50, 50))

    # All text needed during the exam.
    CHECK = small.render("CHECK!", True, colors.BLACK)
    STALEMATE = small.render("STALEMATE!", True, colors.BLACK)
    CHECKMATE = small.render("CHECKMATE!", True, colors.BLACK)
    LOST = small.render("LOST", True, colors.BLACK)
    CHOOSE = small.render("CHOOSE:", True, colors.BLACK)
    UNDO = small.render("Undo", True, colors.BLACK)

    # Quit prompt message.
    MESSAGE = (
        small.render("Do you want to quit", True, colors.WHITE),
        small.render("this game?", True, colors.WHITE),
    )
    # Quit prompot yes/no
    YES = small.render("Yes", True, colors.WHITE)
    NO = small.render("No", True, colors.WHITE)
    TURN = (
        small.render("Other's turn", True, colors.BLACK),
        small.render("Your turn", True, colors.BLACK),
    )


# Main Menu resources

class MAIN:
    # Header
    HEADING = head.render("CHESS", True, colors.WHITE)

    # Window Icon
    ICON = ICON

    # Background
    BG = BGSPRITE.subsurface((0, 0, 500, 500))

    # Play button normal + highlighted
    PLAY = large.render("Play", True, colors.WHITE)
    PLAY_H = large.render("Play", True, colors.GREY)


# Singleplayer Menu Resources

class SINGLE:
    text = ''
    
    # Header
    HEAD = large.render("Singleplayer", True, colors.WHITE)

    # Side choices
    SELECT = SELECT
    # Choose text
    CHOOSE = small.render("Choose:", True, colors.WHITE)

    # Start button
    START = small.render("Start Game", True, colors.GOLD)
    
    # Singleplayer description
    PARA1 = [vsmall.render(line, True, colors.WHITE)
             for line in text.split('\n')]


pygame.font.quit()


