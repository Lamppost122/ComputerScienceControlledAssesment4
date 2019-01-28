import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk

class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        self.titleProfile = ttk.Label(self,text="My Profile",font=controller.title_font)
        self.lblFirstName= ttk.Label(self,text=" First Name :")
        self.lblLastName= ttk.Label(self,text=" Last Name :")
        self.lblPhoneNumber= ttk.Label(self,text=" Phone Number :")
        self.lblAddress= ttk.Label(self,text=" Address :")
        self.lblPostcode= ttk.Label(self,text=" Postcode :")
        self.lblDateOfBirth= ttk.Label(self,text=" Date of Birth :")
        self.lblTeam = ttk.Label(self,text=" Team :")
        self.GetDataButton = ttk.Button(self,text="Get Data",command=self.on_show_frame)
        self.MatchButton =ttk.Button(self,text = "Match Data",command = lambda :controller.show_frame("MatchScreen"))
        self.AdminCommandsButton = ttk.Button(self,text = "AdminCommands",command = lambda:controller.show_frame("AdminCommands"))
        self.NewsButton = ttk.Button(self,text = "News/Updates",command = lambda:controller.show_frame("News"))
        self.BackButton= ttk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))

        self.titleProfile.grid(row = 0 ,column = 0 ,columnspan = 2)
        self.lblFirstName.grid(row=1,column=0)
        self.lblLastName.grid(row=2,column=0)
        self.lblPhoneNumber.grid(row=3,column=0)
        self.lblAddress.grid(row=4,column=0)
        self.lblPostcode.grid(row=5,column=0)
        self.lblDateOfBirth.grid(row=6,column=0)
        self.lblTeam.grid(row=7,column = 0 )
        self.GetDataButton.grid(row=8,column =0)
        self.MatchButton.grid(row = 3,column = 3)
        self.AdminCommandsButton.grid(row=3,column =4)
        self.NewsButton.grid(row=3,column =5)
        self.BackButton.grid(row=3,column = 6)

    def BackButtonRun(self,controller):
        global PagesViewed
        PagesViewed.pop()
        controller.show_frame(PagesViewed[-1])



    def on_show_frame(self):
        global CurrentUser


        with open('players.json', 'r') as fp:
                    player = json.load(fp)

##        with open("team.json","r")as fp:
##            team = json.load(fp)

        Playerdata = player[CurrentUser]

        self.lblDataFirstName= ttk.Label(self,text ="User Data Not Found ")
        self.lblDataLastName= ttk.Label(self,text="User Data Not Found ")
        self.lblDataPhoneNumber= ttk.Label(self,text="User Data Not Found ")
        self.lblDataAddress= ttk.Label(self,text="User Data Not Found ")
        self.lblDataPostcode= ttk.Label(self,text="User Data Not Found ")
        self.lblDataDateOfBirth = ttk.Label(self,text="User Data Not Found ")
        self.lblDataTeam = ttk.Label(self,text=" Team :")

        self.lblDataFirstName.grid(row=1,column=1)
        self.lblDataLastName.grid(row=2,column=1)
        self.lblDataPhoneNumber.grid(row=3,column=1)
        self.lblDataAddress.grid(row=4,column=1)
        self.lblDataPostcode.grid(row=5,column=1)
        self.lblDataDateOfBirth.grid(row=6,column=1)
        self.lblDataTeam.grid(row=7,column = 1 )

        self.lblDataFirstName.config(text = Playerdata["First name"])
        self.lblDataLastName.config(text = Playerdata["Last name"])
        self.lblDataPhoneNumber.config(text = Playerdata["Phone number"])
        self.lblDataAddress.config(text = Playerdata["Address"])
        self.lblDataPostcode.config(text = Playerdata["Post code"])
        self.lblDataDateOfBirth.config(text = Playerdata["Date of Birth"])
        self.lblDataTeam.config(text = Playerdata["First name"]) # Need to change to team when team is implemented


