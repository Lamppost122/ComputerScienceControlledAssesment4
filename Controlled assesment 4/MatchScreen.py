import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk

class MatchScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Title = ttk.Label(self,text = "Matchs" ,font = controller.title_font)
        self.lblTeam = ttk.Label(self,text = "Team: ")
        self.txtTeamNumber = ttk.Entry(self)
        self.GetTeamMatchesButton = ttk.Button(self,text = "Get Team Matches",command=self.get_Team_Matches)
        self.GetMyMatchesButton =ttk.Button(self,text = "Get My Matches")
        self.BackButton= ttk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))
        self.Title.grid(row = 0,column  =0)
        self.lblTeam.grid(row = 1,column  =0)
        self.txtTeamNumber.grid(row = 1,column  =1)
        self.GetTeamMatchesButton.grid(row = 1,column  =2)
        self.GetMyMatchesButton.grid(row = 1,column  =3)
        self.BackButton.grid(row =1 ,column = 4)

    def BackButtonRun(self,controller):
        global PagesViewed
        PagesViewed.pop()
        controller.show_frame(PagesViewed[-1])


    def get_Team_Matches(self):
         TeamNumber = self.txtTeamNumber.get()
         Data = SystemToolKit.readFile("Matches.json")
         print(Data)
         MatchData = Data[TeamNumber]
         MatchData = sorted(MatchData)#by date

         for i ,j in enumerate(MatchData):
            MatchText = ""
            j = ttk.Label(self,text = MatchText)
            j.grid(row = i ,column = 0 )

