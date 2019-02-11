import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config

class Home(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        self.titleProfile = tk.Label(self,text="My Profile",font=controller.title_font)
        self.lblFirstName= tk.Label(self,text=" First Name :")
        self.lblLastName= tk.Label(self,text=" Last Name :")
        self.lblPhoneNumber= tk.Label(self,text=" Phone Number :")
        self.lblAddress= tk.Label(self,text=" Address :")
        self.lblPostcode= tk.Label(self,text=" Postcode :")
        self.lblDateOfBirth= tk.Label(self,text=" Date of Birth :")
        self.lblTeam = tk.Label(self,text=" Team :")
        self.GetDataButton =tk.Button(self,text="Get Data",command=lambda:self.on_show_frame(controller))
        self.MatchButton =tk.Button(self,text = "Match Data",command = lambda :controller.show_frame("MatchScreen"))
        self.AdminCommandsButton = tk.Button(self,text = "AdminCommands",command = lambda:controller.show_frame("AdminCommands"))
        self.NewsButton = tk.Button(self,text = "News/Updates",command = lambda:controller.show_frame("News"))
        self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))

        self.titleProfile.config(background="#f4f8ff",fg = "#485e82",pady="5")

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



    def on_show_frame(self,controller):
        global CurrentUser


        with open('players.json', 'r') as fp:
                    player = json.load(fp)

        with open("team.json","r")as fp:
            team = json.load(fp)
        print team
        try:
            Playerdata = player[Config.CurrentUser]
        except KeyError:
            messagebox.showinfo("Messgae","Please set up your profile")
            controller.show_frame("ProfileSetup")

        self.lblDataFirstName= tk.Label(self,text ="")
        self.lblDataLastName= tk.Label(self,text="")
        self.lblDataPhoneNumber= tk.Label(self,text="")
        self.lblDataAddress= tk.Label(self,text="")
        self.lblDataPostcode= tk.Label(self,text="")
        self.lblDataDateOfBirth = tk.Label(self,text="")
        self.lblDataTeam = tk.Label(self,text="")

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


