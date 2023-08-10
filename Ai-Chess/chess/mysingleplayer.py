'''
In this file, we manage the chess gameplay. 
'''

from chess.lib import *


# Run main code for chess singleplayer

def main(win, player):

    # Draw board and pieces.
    start(win)

    # Moves list when needed for undo.
    moves = []

    # Initialize the positions and flags.
    side, board, flags = initBoardVars()

    clock = pygame.time.Clock()

    # User previous and current input.
    sel = prevsel = [0, 0]
    while True:
        clock.tick(25)
        # Check if the game ended.
        end = isEnd(side, board, flags)

        # Get user input.
        for event in pygame.event.get():

            # Return 0 to main menu if user quits (exit game).
            if event.type == pygame.QUIT and prompt(win):
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Go back to main menu.
                if 455 < x < 495 and 0 < y < 40 and prompt(win):
                    return 1

                # Store the square that the user clicked on.
                if 50 < x < 450 and 50 < y < 450:

                    # Floor of dividing on 50 yields the position of that square.
                    x, y = x // 50, y // 50

                    prevsel = sel
                    sel = [x, y]

                    # Check if last 2 moves yield a valid move.
                    if (side == player and isValidMove(side, board, flags, prevsel, sel)):
                        animate(win, side, board, prevsel, sel)
                        side, board, flags = makeMove(
                            side, board, prevsel, sel, flags)
                        moves.append((prevsel, sel))

                elif side == player or end:
                    sel = [0, 0]

                    # User clicked on undo button.
                    if 5 < x < 70 and 10 < y < 40 and not end:
                        side, board, flags, moves = undo(moves)
        # Show screen after handling user input.
        showScreen(win, side, board, flags, sel, player)

        end = isEnd(side, board, flags)

        # If the game is not over, process AI turn.
        if side != player and not end:

        
            # Choose a move using the algorithm.
            fro, to = miniMax(side, board, flags)

            animate(win, side, board, fro, to)
            side, board, flags = makeMove(side, board, fro, to, flags)
            moves.append((fro, to))
            sel = [0, 0]
