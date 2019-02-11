import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *

class RemoveMatch(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title = ttk.Label(self,text = "Remove Match" ,font = controller.title_font)
            self.lblTeam = ttk.Label(self,text = "Team: ")
            self.txtTeam = ttk.Entry(self)
            self.getMatchesButton = ttk.Button(self,text = "Get Matches",command = self.GetMatches)
            self.MatchList = tk.Listbox(self)
            b = ttk.Button(self, text="Remove  Match",command=self.RemoveMatch )
            self.BackButton= ttk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))
            b.grid(row = 2,column = 4)


            self.Title.grid(row = 0,column = 0,columnspan = 3)
            self.lblTeam.grid(row = 1,column = 0)
            self.txtTeam.grid(row = 1,column = 1 )
            self.getMatchesButton.grid(row= 1 , column = 2)
            self.MatchList.grid(row = 2,column = 0,columnspan = 3)
            self.BackButton.grid(row =2,column = 3)

        def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])




        def GetMatches(self):
            self.MatchList.delete(0,tk.END)

            self.teamMatches = SystemToolKit.readFile("matches.json")
            self.matches = self.teamMatches[self.txtTeam.get()]
            self.orderedList = []


            for item in self.matches:
                self.orderedList.append(item)
                text = str(self.txtTeam.get()) +" vs " +self.matches[item]["Opposition"]+" on " +self.matches[item]["Date"]
                self.MatchList.insert(tk.END,text)


        def RemoveMatch(self):
            self.matches.pop(self.orderedList[self.MatchList.index(tk.ANCHOR)], None)
            self.MatchList.delete(tk.ANCHOR)
            self.teamMatches[self.txtTeam.get() ] = self.matches
            with open("matches.json","w+")as fp:
                json.dump(self.teamMatches,fp)


