
from tkinter import *
from tkinter import ttk
import os, sys, inspect

class CreateFrame():
    def __init__(self, root):
        """ Create operation frame"""
        self.operationsFrame = Frame(root, width=200)
        self.operationsFrame.grid(row=0, column=0, padx=(3,1), pady=1, sticky='nswe')