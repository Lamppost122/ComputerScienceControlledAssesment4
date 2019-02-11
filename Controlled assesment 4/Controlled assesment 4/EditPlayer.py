import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *

class EditPlayer(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.StartCount = 3
            self.Title = tk.Label(self,text = "Edit player details" ,font = controller.title_font)
            self.lblPlayer = ttk.Label(self,text = "Player: ")
            self.txtPlayer = ttk.Entry(self)
            self.getPlayerButton = tk.Button(self,text = "Get Players",command = self.GetPlayers)
            self.EditPlayerButton = tk.Button(self,text = "Edit Players",command = self.Edit_Players)
            self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))

            self.Title.config(background="#f4f8ff",fg = "#485e82",pady="5")
            self.Title.grid(row =0,column =0,columnspan = 4)
            self.lblPlayer.grid(row =1,column =0)
            self.txtPlayer.grid(row =1,column =1)
            self.getPlayerButton.grid(row =1,column =2)
            self.EditPlayerButton.grid(row =1,column =3)
            self.BackButton.grid(row =1,column = 4)

        def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])



        def GetPlayers(self):
            self.orderedList = []


            self.players = SystemToolKit.readFile("players.json")
            print(self.players)



            for i ,j in enumerate(self.players):
                self.orderedList.append(j)
                self.txtFirstName = ttk.Entry(self)
                self.txtLastName = ttk.Entry(self)
                self.txtPhoneNumber = ttk.Entry(self)
                self.txtAddress = ttk.Entry(self)
                self.txtPostcode = ttk.Entry(self)
                self.txtDateOfBirth = ttk.Entry(self)
                self.txtFirstName.grid(row = self.StartCount+i, column  =0 )
                self.txtLastName.grid(row = self.StartCount+i,column = 1)
                self.txtPhoneNumber.grid(row = self.StartCount+i, column  =2 )
                self.txtAddress.grid(row = self.StartCount + i, column  =3 )
                self.txtPostcode.grid(row = self.StartCount + i, column  =4 )
                self.txtDateOfBirth.grid(row = self.StartCount + i, column  =5 )
                self.txtFirstName.insert(0,self.players[j]["First name"])
                self.txtLastName.insert(0,self.players[j]["Last name"])
                self.txtPhoneNumber.insert(0,self.players[j]["Phone number"])
                self.txtAddress.insert(0,self.players[j]["Address"])
                self.txtPostcode.insert(0,self.players[j]["Post code"])
                self.txtDateOfBirth.insert(0,self.players[j]["Date of Birth"])
            self.orderedList = list(reversed(self.orderedList))

        def Edit_Players(self):


                count = 0

                data = []

                for i,j in enumerate(self.grid_slaves()):

                    if int(j.grid_info()["row"]) >= self.StartCount:


                        try:

                            data.append(j.get())
                            if len(data) == 6 :
                                data =  list(reversed(data))
                                self.players[self.orderedList[count]]["First name"] = data[0]
                                self.players[self.orderedList[count]]["Last name"] = data[1]
                                self.players[self.orderedList[count]]["Phone number"] = data[2]
                                self.players[self.orderedList[count]]["Address"] = data[3]
                                self.players[self.orderedList[count]]["Post code"] = data[4]
                                self.players[self.orderedList[count]]["Date of Birth"] = data[5]
                                count +=1
                                data = []


                        except :AttributeError

                with open('players.json', 'w') as fp:
                    json.dump(self.players,fp)
