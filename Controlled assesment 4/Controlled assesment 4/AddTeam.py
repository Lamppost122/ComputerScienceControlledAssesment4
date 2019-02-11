import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *

class AddTeam(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller

            self.TeamPlayers = []
            self.orderedList = []
            self.Title = tk.Label(self,text = "Create Team" ,font = controller.title_font)
            self.lblPlayerName = ttk.Label(self,text = "Player Name: ")
            self.lblPlayer = ttk.Label(self,text = "Players ")
            self.lblTeam = ttk.Label(self,text="Team")
            self.txtTeamNumber = ttk.Entry(self)
            self.lblTeamNumber = ttk.Label(self,text="Team Number: ")
            self.txtPlayer = ttk.Entry(self)
            self.getPlayerButton = tk.Button(self,text = "Get Player",command = self.GetPlayer)
            self.PlayerList = tk.Listbox(self)
            self.TeamList = tk.Listbox(self)
            b = tk.Button(self, text="Move Player",command=self.MovePlayer )
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))
            self.RemovePlayerButton = tk.Button(self,text= "Remove Player",command = self.RemovePlayer)
            self.SaveButton = tk.Button(self,text = "Save",command = self.SaveTeam)

            self.Title.config(background="#f4f8ff",fg = "#485e82",pady="5")



            self.Title.grid(row = 0,column = 0,columnspan = 3)
            self.lblPlayerName.grid(row = 1,column = 0)
            self.txtPlayer.grid(row = 1,column = 1 )
            self.getPlayerButton.grid(row= 1 , column = 2)
            self.lblTeamNumber.grid(row= 1,column = 4)
            self.txtTeamNumber.grid(row= 1 ,column =5)
            self.lblPlayer.grid(row = 2,column = 1)
            self.lblTeam.grid(row= 2,column = 3)
            self.PlayerList.grid(row = 3,column = 1)
            b.grid(row = 3,column = 2)
            self.TeamList.grid(row = 3 ,column = 3 )
            self.RemovePlayerButton.grid(row =3,column = 4)
            self.SaveButton.grid(row = 3,column = 5)
            self.BackButton.grid(row =1,column = 3)

        def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])

        def SaveTeam(self):
            Team = SystemToolKit.readFile("team.json")

            TeamId = uuid.uuid4()
            Data = {}
            for i ,j in enumerate(self.TeamPlayers):
                Data[i] = j
            Data["Team Number"] = self.txtTeamNumber.get()
            Team[str(TeamId)] = Data

            with open("Team.json","w") as fp:
                json.dump(Team,fp)
            self.controller.show_frame("Home")






        def GetPlayer(self):
            self.PlayerList.delete(0,tk.END)
            data =self.txtPlayer.get()
            data = data.lower()



            self.allPlayers = SystemToolKit.readFile("players.json")


            for i,j in enumerate(self.allPlayers):
                if self.allPlayers[j]["First name"].lower() == data or self.allPlayers[j]["Last name"].lower() == data or self.allPlayers[j]["First name"].lower() + " " + self.allPlayers[j]["Last name"].lower() == data:

                    self.orderedList.append(j)
                    text = str(self.allPlayers[j]["First name"]) + " " + str(self.allPlayers[j]["Last name"])
                    self.PlayerList.insert(tk.END,text)






        def MovePlayer(self):
            if self.PlayerList.index(tk.ANCHOR) < len(self.orderedList):
                j = self.orderedList[self.PlayerList.index(tk.ANCHOR)]
                text = str(self.allPlayers[j]["First name"]) + " " + str(self.allPlayers[j]["Last name"])
                self.TeamPlayers.append(j)
                self.orderedList.pop()
                self.TeamList.insert(tk.END,text)
                self.PlayerList.delete(tk.ANCHOR)

        def RemovePlayer(self):
            if self.TeamList.index(tk.ANCHOR) < len(self.TeamPlayers):
                j = self.TeamPlayers[self.TeamList.index(tk.ANCHOR)]
                text = str(self.allPlayers[j]["First name"]) + " " + str(self.allPlayers[j]["Last name"])
                self.orderedList.append(j)
                self.TeamPlayers.pop()
                self.PlayerList.insert(tk.END,text)
                self.TeamList.delete(tk.ANCHOR)


