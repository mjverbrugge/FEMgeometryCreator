
from tkinter import *
from tkinter import ttk
import os, sys, inspect

class CreateFrame():
    def __init__(self, root):
        """ Create property frame"""
        self.vpButtonFrame = Frame(root, width=25)
        self.vpButtonFrame.grid(row=0, column=2, padx=(1,1), pady=1, sticky='nswe')