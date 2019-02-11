import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *



class RemovePlayer(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title = ttk.Label(self,text = "Remove Player" ,font = controller.title_font)
            self.lblPlayer = ttk.Label(self,text = "Player Name: ")
            self.txtPlayer = ttk.Entry(self)
            self.getPlayerButton = ttk.Button(self,text = "Get Player",command = self.GetPlayer)
            self.PlayerList = tk.Listbox(self)
            b = ttk.Button(self, text="Remove  Player",command=self.RemovePlayer )
            self.BackButton= ttk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))
            b.grid(row = 2,column = 4)


            self.Title.grid(row = 0,column = 0,columnspan = 3)
            self.lblPlayer.grid(row = 1,column = 0)
            self.txtPlayer.grid(row = 1,column = 1 )
            self.getPlayerButton.grid(row= 1 , column = 2)
            self.PlayerList.grid(row = 2,column = 0,columnspan = 3)
            self.BackButton.grid(row =2,column = 3)

        def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])




        def GetPlayer(self):
            self.PlayerList.delete(0,tk.END)
            data =self.txtPlayer.get()
            data = data.lower()



            self.allPlayers = SystemToolKit.readFile("players.json")
            self.orderedList = []

            for i,j in enumerate(self.allPlayers):
                if self.allPlayers[j]["First name"].lower() == data or self.allPlayers[j]["Last name"].lower() == data or self.allPlayers[j]["First name"].lower() + " " + self.allPlayers[j]["Last name"].lower() == data:

                    self.orderedList.append(j)
                    text = str(self.allPlayers[j]["First name"]) + " " + str(self.allPlayers[j]["Last name"])
                    self.PlayerList.insert(tk.END,text)



        def RemovePlayer(self):
            self.allPlayers.pop(self.orderedList[self.PlayerList.index(tk.ANCHOR)], None)
            self.PlayerList.delete(tk.ANCHOR)

            with open("players.json","w+")as fp:
                json.dump(self.allPlayers,fp)

