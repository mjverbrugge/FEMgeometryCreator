
from tkinter import *
from tkinter import ttk
import os, sys, inspect

class CreateFrame():
    def __init__(self, root):
        """ Create property frame"""
        self.propertyFrame = Frame(root, width=240, bd=1, relief='raised')
        self.propertyFrame.grid(row=0, rowspan=3, column=3, padx=(1,3), pady=1, sticky='nswe')