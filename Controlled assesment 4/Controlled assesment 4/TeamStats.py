import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from SystemToolKit import *
from Gui import *

class TeamStats(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        with open("playerStats.json") as fp:
            data= json.load(fp)
        print(data)