import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *

class EditMatch(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.StartCount = 2
            self.Title = tk.Label(self,text = "Edit Match" ,font = controller.title_font)
            self.lblTeam = ttk.Label(self,text = "Team: ")
            self.txtTeam = ttk.Entry(self)
            self.getMatchesButton = tk.Button(self,text = "Get Matches",command = self.GetMatches)
            self.EditMatchButton = tk.Button(self,text = "Edit Matches",command = self.Edit_Match)
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))

            self.Title.config(background="#f4f8ff",fg = "#485e82",pady="5")
            self.Title.grid(row =0,column =0)
            self.lblTeam.grid(row =1,column =0)
            self.txtTeam.grid(row =1,column =1)
            self.getMatchesButton.grid(row =1,column =2)
            self.EditMatchButton.grid(row =1,column =3)
            self.BackButton.grid(row =1,column = 4)

        def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])



        def GetMatches(self):
            self.orderedList = []


            with open("matches.json","r")as fp:
                matches = json.load(fp)

            self.teamMatches = matches[self.txtTeam.get()]

            for i ,j in enumerate(self.teamMatches):
                self.orderedList.append(j)
                self.txtOpposition=ttk.Entry(self)
                self.txtDate = ttk.Entry(self)
                self.txtTime = ttk.Entry(self)
                self.txtLocation = ttk.Entry(self)
                self.txtOpposition.grid(row = self.StartCount+i, column  =0 )
                self.txtDate.grid(row = self.StartCount+i,column = 1)
                self.txtTime.grid(row = self.StartCount+i, column  =2 )
                self.txtLocation.grid(row = self.StartCount + i, column  =3 )
                self.txtOpposition.insert(0,self.teamMatches[j]["Opposition"])
                self.txtDate.insert(0,self.teamMatches[j]["Date"])
                self.txtTime.insert(0,self.teamMatches[j]["Time"])
                self.txtLocation.insert(0,self.teamMatches[j]["Location"])
            self.orderedList = list(reversed(self.orderedList))

        def Edit_Match(self):


                count = 0

                data = []
                for i,j in enumerate(self.grid_slaves()):
                    if int(j.grid_info()["row"]) >= self.StartCount:

                        try:

                            data.append(j.get())
                            if len(data) == 4 :
                                data =  list(reversed(data))
                                self.teamMatches[self.orderedList[count]]["Opposition"] = data[0]
                                self.teamMatches[self.orderedList[count]]["Location"] = data[3]
                                self.teamMatches[self.orderedList[count]]["Time"] = data[2]
                                self.teamMatches[self.orderedList[count]]["Date"] = data[1]
                                count +=1
                                data = []


                        except :AttributeError
                with open('matches.json', 'w') as fp:
                    json.dump(self.teamMatches,fp)

