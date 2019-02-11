import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *

class RemoveTeam(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title = ttk.Label(self,text = "Remove Team" ,font = controller.title_font)
            self.getTeamButton = ttk.Button(self,text = "Get Teams",command = self.GetTeam)
            self.TeamList = tk.Listbox(self)
            b = ttk.Button(self, text="Remove Team",command=self.RemoveTeam )
            self.BackButton= ttk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))
            b.grid(row = 2,column = 4)


            self.Title.grid(row = 0,column = 0,columnspan = 3)
            self.getTeamButton.grid(row= 1 , column = 2)
            self.TeamList.grid(row = 2,column = 0,columnspan = 3)
            self.BackButton.grid(row =2,column = 3)

        def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])




        def GetTeam(self):
            self.TeamList.delete(0,tk.END)
            self.teams = SystemToolKit.readFile("Team.json")
            self.orderedList = []
            for item in self.teams:
                self.orderedList.append(item)
                text = self.teams[item]["Team Number"]
                self.TeamList.insert(tk.END,text)


        def RemoveTeam(self):
            del self.teams[self.orderedList[self.TeamList.index(tk.ANCHOR)]]
            self.orderedList.pop(self.TeamList.index(tk.ANCHOR))
            self.TeamList.delete(tk.ANCHOR)
            with open("Team.json","w+")as fp:
                json.dump(self.teams,fp)
