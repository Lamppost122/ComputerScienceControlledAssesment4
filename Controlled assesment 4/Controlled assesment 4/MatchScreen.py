import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *

class MatchScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.Title = tk.Label(self,text = "Matchs" ,font = controller.title_font)
        self.lblTeam = ttk.Label(self,text = "Team: ")
        self.txtTeamNumber = ttk.Entry(self)
        self.GetTeamMatchesButton = tk.Button(self,text = "Get Team Matches",command=self.get_Team_Matches)
        self.GetMyMatchesButton =tk.Button(self,text = "Get My Matches",command =self.GetMyMatches)
        self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))
        self.Title.config(background="#f4f8ff",fg = "#485e82",pady="5")
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
         Data = SystemToolKit.readFile("matches.json")
         TeamID = self.GetTeamID(TeamNumber)
         MatchData = Data[TeamID]
         print MatchData

         for i ,j in enumerate(MatchData):
            MatchText = "Oposition: "+MatchData[j]["Opposition"] +"    Data: "+ MatchData[j]['Date']+"   Time: "+ MatchData[j]["Time"]+"   Location: "+ MatchData[j]["Location"]
            j = tk.Label(self,text = MatchText)
            j.grid(row = i+2 ,column = 0 ,columnspan=5)
    @staticmethod
    def GetTeamID(TeamNumber):
        Teams = SystemToolKit.readFile("team.json")
        for i in Teams:
            if Teams[i]["Team Number"] == str(TeamNumber):

                return i
    def GetMyTeam(self):
        Data = SystemToolKit.readFile("teams.json")
        for i in Data:
            if Data[i]==Config.CurrentUser:
                return i
    def GetMyMatches(self):
         TeamID = self.geMyTeam()


         Data = SystemToolKit.readFile("matches.json")

         MatchData = Data[TeamID]
         print MatchData

         for i ,j in enumerate(MatchData):
            MatchText = "Oposition: "+MatchData[j]["Opposition"] +"    Data: "+ MatchData[j]['Date']+"   Time: "+ MatchData[j]["Time"]+"   Location: "+ MatchData[j]["Location"]
            j = tk.Label(self,text = MatchText)
            j.grid(row = i+2 ,column = 0 ,columnspan=5)

