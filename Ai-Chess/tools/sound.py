"""
Handling all sound related stuff.
"""

import os.path

try:
    import pygame.mixer
    pygame.mixer.init()
    
    SUCCESS = pygame.mixer.get_init() is not None

except (ImportError, RuntimeError):
    SUCCESS = False

if SUCCESS:
    background = pygame.mixer.Sound(os.path.join("res", "sounds", "background.ogg"))

if SUCCESS:
    pygame.mixer.quit()
