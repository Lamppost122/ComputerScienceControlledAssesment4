import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *

class AddMatch(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title = tk.Label(self,text = "Add Match" ,font = controller.title_font)

            self.lblTeam= ttk.Label(self,text="Team: ")
            self.lblLocation =ttk.Label(self,text="Location: ")
            self.lblTime = ttk.Label(self,text="Time: ")
            self.lblDay = ttk.Label(self,text="Day: ")
            self.lblOpposition = ttk.Label(self,text="Opposition: ")
            self.txtTeam = ttk.Entry(self)
            self.txtLocation = ttk.Entry(self)
            self.txtTime = ttk.Entry(self)
            self.txtDate = ttk.Entry(self)
            self.txtOpposition = ttk.Entry(self)
            self.AddMatchButton = tk.Button(self,text="Add Match",command = lambda:self.AddMatch(controller))
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))

            self.Title.config(background="#f4f8ff",fg = "#485e82",pady="5")

            self.Title.grid(row=0,column =0,columnspan = 2)
            self.lblTeam.grid(row=1,column=0)
            self.lblLocation.grid(row=2,column=0)
            self.lblTime.grid(row=3,column=0)
            self.lblDay.grid(row=4,column=0)
            self.lblOpposition.grid(row=5,column=0)
            self.txtTeam.grid(row = 1,column = 1)
            self.txtLocation.grid(row = 2,column = 1)
            self.txtTime.grid(row = 3,column = 1)
            self.txtDate.grid(row = 4,column = 1)
            self.txtOpposition.grid(row = 5,column = 1)
            self.AddMatchButton.grid(row = 6,column = 1 ,columnspan = 1 )
            self.BackButton.grid(row = 6,column = 0)
        def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])


        def AddMatch(self,controller):

            Team , Location, Time, Date, Opposition = self.getMatchData()

            data = {}


            if self.validMatchData(Team , Location, Time, Date, Opposition) == True :



                match = SystemToolKit.readFile("matches.json")
                TeamId = self.getTeamId(Team)

                teamMatches = self.getTeamMatches(match,TeamId)


                matchID = str(uuid.uuid4())
                data["Opposition"] = Opposition
                data["Location"] = Location
                data["Time"] = Time
                data["Date"] = Date
                teamMatches[matchID] = data

                match[TeamId] = teamMatches
                print(match)

                with open('matches.json', 'w+') as fp:
                    json.dump(match, fp)
                controller.show_frame("Home")

        def getTeamId(self,TeamNumber):
            Teams = SystemToolKit.readFile("team.json")
            for i in Teams:
                if Teams[i]["Team Number"] == TeamNumber:
                    return i

        def getTeamMatches(self,match,TeamId):
            for i in match :
                if i == TeamId :
                    return match[TeamID]
            return {}





        def getMatchData(self):
            Team =self.txtTeam.get()
            Location = self.txtLocation.get()
            Time = self.txtTime.get()
            Date = self.txtDate.get()
            Opposition = self.txtOpposition.get()
            return Team , Location, Time, Date, Opposition

        def validMatchData(self,Team , Location, Time, Day, Opposition):
            return True

