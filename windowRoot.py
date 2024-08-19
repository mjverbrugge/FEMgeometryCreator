"""
Compressed code to create a pygame screen in a tkinter window.

returns:
-root       : main tkinter root
-rootframes : instance containing the frameViewport frame
-screen     : pygame screen instance
"""

# Imports general
from tkinter import *
import pygame
import os

# Import user
from windowFrames import operations
from windowFrames import properties
from windowFrames import viewportButtons

###
## FUNCTIONS
###

def rootConfiguration(root):
    """ Main window root configuration"""

    root.title('FEM 2D Geometry Creator v0.0.0')
    root.geometry('900x500')
    
    root.columnconfigure(0, weight=0)   # Left category/object window indicated as side tree
    root.columnconfigure(1, weight=1)   # Main viewport
    root.columnconfigure(2, weight=0)   # Viewport buttons
    root.columnconfigure(3, weight=0)   # Edit and info column
    
    root.rowconfigure(0, weight=1)      # General row

    return root


###
## CLASSES
###

class mainRoot:
    """ Main frame instance to root """

    def __init__(self, root):
        """Construct the initial tkinter frames"""
        rootConfiguration(root)

        # Flexible frames    
        self.operations = operations.CreateFrame(root)
        self.properties = properties.CreateFrame(root)
        self.viewportButtons = viewportButtons.CreateFrame(root)

        # Add viewport frame
        self.viewport = Frame(root, bg='blue')
        self.viewport.grid(row=0, column=1, padx=1, pady=1, sticky='nswe')


###
## MAIN
###

# Tkinter
root = Tk()
rootFrames = mainRoot(root)

# Pygame screen
os.environ['SDL_WINDOWID'] = str(rootFrames.viewport.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.display.init()
screen = pygame.display.set_mode()