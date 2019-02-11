import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *

class News(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Title = tk.Label(self,text ="News/Updates",font = controller.title_font)
        self.Title.config(background="#f4f8ff",fg = "#485e82",pady="5")
        self.Title.grid(row =0,column =0 )
        self.startCount = 2
        self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))
        self.BackButton.grid(row =1,column = 0)

    def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])








    def write_News_to_screen(self):
        updates = SystemToolKit.readFile("updates.json")

        for i in updates:

            j = ttk.Label(self,text = updates[i]["Data"])
            k = ttk.Label(self,text= "Update: "+updates[i]["Date"])

            j.grid(row = 2 *(len(updates)-int(i)+self.startCount),columnspan =2,column  =0)
            k.grid(row =2 *(len(updates)-int(i)+self.startCount) + 1,columnspan =2,column  =0 )

