import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *

class AddNews(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.addUpdateButton =tk.Button(self,text = "Add update",command = self.AddUpdate)
        self.lblAddUpdate = tk.Label(self,text = "Enter News/Update bellow",font=controller.title_font)
        self.txtAddUpdate =tk.Text(self,width="50",height = "10")
        self.BackButton= tk.Button(self, text="Back",command=lambda:self.BackButtonRun(controller))

        self.lblAddUpdate.config(background="#f4f8ff",fg = "#485e82",pady="5")
        self.txtAddUpdate.config(background="white",padx="10")

        self.lblAddUpdate.grid(row = 0,column =0 )
        self.txtAddUpdate.grid(row = 1,column = 0)
        self.addUpdateButton.grid(row=1,column =1)
        self.BackButton.grid(row =1,column = 2)


    def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])


    def AddUpdate(self):

        with open('updates.json') as fp:
                updates= json.load(fp)
        index = 0
        for i,j in enumerate(list(((updates).keys()))):
            if index <= int(j):
                index =int(j) + 1
        updates[index] = {"Data":self.txtAddUpdate.get("1.0",'end-1c'),"Date":str(datetime.date.today())}
        with open('updates.json',"w") as fp:
                json.dump(updates,fp)

