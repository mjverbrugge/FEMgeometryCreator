"""

"""

# General imports
from tkinter import *
from tkinter import ttk
import pygame
from pygame.locals import *

# Local imports
import windowRoot as wR


###
## PYGAME SCREEN REFRESH
###

def pygameLoop():
    """Main pygame function to update the screen"""

    # Create new/emtpy white fill
    wR.screen.fill('white')

    # Update screen
    pygame.display.flip()
    wR.root.update()  
    wR.root.after(10, pygameLoop)