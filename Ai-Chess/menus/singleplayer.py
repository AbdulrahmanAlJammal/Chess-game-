'''
In this file, we manage the single player menu which is called when user clicks
play button on main menu.
'''

import random
import pygame
from tools import colors
from tools.loader import SINGLE, BACK


# This shows the screen
def showScreen(win, select):

    # Fill background with black.
    win.fill((0, 0, 0))

    # # Draw header with rectangle around it.
    # pygame.draw.rect(win, colors.WHITE, (70, 5, 340, 70), 3)
    # win.blit(SINGLE.HEAD, (100, 7))

    # Draw back button.
    win.blit(BACK, (455, 0))

    # # Draw box around all upcoming text.
    # pygame.draw.rect(win, colors.WHITE, (10, 150, 480, 200), 3)

    # Draw each line from the text on a seperate line.
    for line, txt in enumerate(SINGLE.PARA1):
        y = 155 + line * 17
        win.blit(txt, (20, y))

    # Draw choose + selection pieces.
    win.blit(SINGLE.CHOOSE, (90, 240))
    win.blit(SINGLE.SELECT, (200, 230))

    # Draw box around selection.
    pygame.draw.rect(win, colors.PURPLE, (200 + select*50, 230, 50, 50), 3)

    # Draw start button with rectangle around it.
    pygame.draw.rect(win, colors.WHITE, (162, 300, 150, 40), 3)
    win.blit(SINGLE.START, (185, 305))


# This is the main function, called from main menu
def main(win):

    # Variable used for storing user's side choice.
    select = 0
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        showScreen(win, select)

        # Get user input
        for event in pygame.event.get():

            # If user decides to quit the program, return 0 to main menu to indicate the quiting.
            if event.type == pygame.QUIT:
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # User clicked on back
                if 455 < x < 495 and 0 < y < 40:
                    return 1

                # User clicked on one of the selection pieces. Store their choice.
                if 230 < y < 280 and 200 < x < 350:
                    select = (x // 50) - 4

                # User clicked on start game.
                if 170 < x < 310 and 300 < y < 340:
                    
                    # Returning true to main menu indicates user clicked on start game button.
                    if select == 2:
                        return True, random.randint(0, 1)
                    else:
                        return True, select
                        
        # Update the screen every frame
        pygame.display.update()
