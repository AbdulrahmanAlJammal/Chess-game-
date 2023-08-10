"""
This is the main file of the program. It handles running and closing the window.
"""
import pygame
from chess.mysingleplayer import main as startGame
from menus.singleplayer import main as splayermenu
from tools.loader import MAIN
from tools.sound import background


# Some initialisation
pygame.init()
clock = pygame.time.Clock()
# background.play(-1)

# Initialise display, set the caption and icon. Use SCALED if on pygame 2.
if pygame.version.vernum[0] >= 2:
    win = pygame.display.set_mode((500, 500), pygame.SCALED)
else:
    win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ai-Chess")
pygame.display.set_icon(MAIN.ICON)

# Play button position
playPos = (205, 400, 100, 50)


# This is the function that displays the main screen.
def showMain():

    # Now blit all the texts onto the screen one by one

    # Background
    win.blit(MAIN.BG, (0, 0))

    # Header
    win.blit(MAIN.HEADING, (170, 20))

    # # Header Underline
    # pygame.draw.line(win, (255, 255, 255), (40, 105), (190, 105), 4)
    

    # Play Button
    win.blit(MAIN.PLAY, playPos[:2])

# Variable to determine when to close the program.
run = True

while run:
    # Start the game loop at 30fps, show the screen every time at first
    clock.tick(30)
    showMain()

    # We need to get the position of the mouse so that we can blit an image
    # on the text over which the mouse hovers
    x, y = pygame.mouse.get_pos()

    if playPos[0] < x < sum(playPos[::2]) and playPos[1] < y < sum(playPos[1::2]):
        win.blit(MAIN.PLAY_H, playPos[:2])

    # Begin pygame event loop to catch all events
    for event in pygame.event.get():

        # Break from loop if the user clicks on quit button.
        if event.type == pygame.QUIT:
            run = False

        # User has clicked somewhere, determine which button and
        # call a function to handle the game into a different window.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # Player clicked on play button.
            if playPos[0] < x < sum(playPos[::2]) and playPos[1] < y < sum(playPos[1::2]):
                ret = splayermenu(win)

                # User chose to quit game while in singleplayer menu.
                if ret == 0:
                    run = False
                    
                # User chose a side and clicked on start game.
                elif ret != 1:
                    run = startGame(win, ret[1])

    # Update the screen every frame
    pygame.display.flip()

# Stop music, quit pygame after the loop is done
# background.stop()
pygame.quit()
