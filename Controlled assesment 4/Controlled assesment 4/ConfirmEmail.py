import tkinter as tk
import json

import tkinter as tk
from tkinter import font  as tkfont
from tkinter import  messagebox
from tkinter import ttk
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from SystemToolKit import *
from Login import *
import Config




class ConfirmEmail(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.title =tk.Label(self,text = "Confirm email" ,font = controller.title_font)
        self.lblText =tk.Label(self,text="Please enter in the code sent to your email address")
        self.txtConfirm =ttk.Entry(self)
        self.ConfirmButton=tk.Button(self,text ="Confirm",command=lambda:self.CheckConfirmEmail("data.json",controller))
        self.title.grid(row=0,column=0,columnspan = 2)
        self.lblText.grid(row=1,column=0,columnspan=2)
        self.txtConfirm.grid(row=2,column =0)
        self.ConfirmButton.grid(row=2,column =1 )



    def CheckConfirmEmail(self,FileName,controller):
        global CurrentUser
        print Config.CurrentUser
        with open(FileName)as fp:
            Data = json.load(fp)
        print Data[Config.CurrentUser]["Confirmation code"], self.txtConfirm.get()
        if Data[Config.CurrentUser]["Confirmation code"] == self.txtConfirm.get():
            Data[Config.CurrentUser]["ValidEmail"] = True
            controller.show_frame("Login")
            with open(FileName,"w") as fp:
                json.dump(Data,fp)
        else:
            messagebox.showinfo("Messgae","Code Incorrect")

