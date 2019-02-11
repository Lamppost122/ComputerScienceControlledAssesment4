import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *


class AdminCommands(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title =tk.Label(self,text="Admins commands",font = controller.title_font)
            self.lblplayer = ttk.Label(self,text = "Player tools")
            self.lblMatches =ttk.Label(self,text = "Match tools")
            self.lblTeam =ttk.Label(self,text = "Team tools")
            self.lblUpdates = ttk.Label(self,text = "Update/news tools")
            self.RemovePlayerButton = tk.Button(self,text="Remove player",command = lambda: controller.show_frame("RemovePlayer"))
            self.EditPlayerButton = tk.Button(self,text="Edit player",command = lambda: controller.show_frame("EditPlayer"))
            self.AddMatchButton = tk.Button(self,text="Add Match",command = lambda: controller.show_frame("AddMatch"))
            self.RemoveMatchButton = tk.Button(self,text="Remove Match",command = lambda: controller.show_frame("RemoveMatch"))
            self.EditMatchButton = tk.Button(self,text="Edit Match",command = lambda: controller.show_frame("EditMatch"))
            self.AddTeamButton = tk.Button(self,text="Add Team",command = lambda: controller.show_frame("AddTeam"))
            self.RemoveTeamButton = tk.Button(self,text="Remove Team",command = lambda: controller.show_frame("RemoveTeam"))
            self.EditTeamButton = tk.Button(self,text="Edit Team",command = lambda: controller.show_frame("EditTeam"))
            self.AddUpdateButton = tk.Button(self,text="Add Update",command = lambda: controller.show_frame("AddNews"))
            self.RemoveUpdateButton = tk.Button(self,text="Remove Update")
            self.EditUpdateButton = tk.Button(self,text="Edit Update")
            self.BackUpButton = tk.Button(self,text="BackUp",command = lambda: controller.show_frame("BackUp"))
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))

            self.RemovePlayerButton.config(width="15")
            self.EditPlayerButton.config(width="15")
            self.AddMatchButton.config(width="15")
            self.RemoveMatchButton.config(width="15")
            self.EditMatchButton.config(width="15")
            self.AddTeamButton.config(width="15")
            self.RemoveTeamButton.config(width="15")
            self.EditTeamButton.config(width="15")
            self.AddUpdateButton.config(width="15")
            self.RemoveUpdateButton.config(width="15")
            self.EditUpdateButton.config(width="15")
            self.BackUpButton.config(width="15")
            self.BackButton.config(width="15")



            self.Title.grid(row=0,column = 0,columnspan = 4)
            self.lblplayer.grid(row=1,column = 0)
            self.lblMatches.grid(row=1,column = 1)
            self.lblTeam .grid(row=1,column = 2)
            self.lblUpdates.grid(row=1,column = 3)
            self.RemovePlayerButton.grid(row=3,column = 0)
            self.EditPlayerButton.grid(row=4,column = 0)
            self.AddMatchButton.grid(row=2,column = 1)
            self.RemoveMatchButton.grid(row=3,column = 1)
            self.EditMatchButton.grid(row=4,column = 1)
            self.AddTeamButton.grid(row=2,column = 2)
            self.RemoveTeamButton.grid(row=3,column = 2)
            self.EditTeamButton.grid(row=4,column = 2)
            self.AddUpdateButton.grid(row=2,column = 3)
            self.RemoveUpdateButton.grid(row=3,column = 3)
            self.EditUpdateButton.grid(row=4,column = 3)
            self.BackUpButton.grid(row=4,column =4)
            self.BackButton.grid(row =1,column = 5)


        def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])

