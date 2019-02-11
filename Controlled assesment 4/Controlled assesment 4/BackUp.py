import os
import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
import shutil
import datetime

class BackUp(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title =tk.Label(self,text="BackUps",font = controller.title_font)
            self.PastBackupsList = tk.Listbox(self)
            self.getBackupListButton = tk.Button(self,text="Get Back Ups",command = lambda: self.writeToScreen("BackupList.json"))
            self.createBackUpButton = tk.Button(self,text="Create Back up",command =lambda: self.createBackUp("BackupList.json"))
            self.recoverBackUpButton = tk.Button(self,text="Recover Back up",command =lambda: self.RecoverBackUp("BackupList.json"))
            self.BackButton = tk.Button(self,text = "Back",command = lambda:self.BackButtonRun(controller))
            self.Title.config(background="#f4f8ff",fg = "#485e82",pady="5")
            self.PastBackupsList.config(background="white")
            self.Title.grid(row = 0,column =0)
            self.PastBackupsList.grid(row= 1,column= 0)
            self.getBackupListButton.grid(row = 1,column =1)
            self.createBackUpButton.grid(row=1,column = 2)
            self.recoverBackUpButton.grid(row=1,column = 3)

        def BackButtonRun(self,controller):
            global PagesViewed
            PagesViewed.pop()
            controller.show_frame(PagesViewed[-1])

        def writeToScreen(self,FileName):
            self.PastBackupsList.delete(0,tk.END)
            with open(FileName)as fp:
                Data = json.load(fp)
            for i in Data:
                self.PastBackupsList.insert(0,i)

        def createBackUp(self,FileName):
            with open(FileName)as fp:
                Data = json.load(fp)
            today = datetime.datetime.today()
            today = today.strftime("%d/%m/%y-%H:%M")
            FileType = ["Child","Parent","Grandparent"]
            Names = []

            for i in FileType:
                for j in Data[i]:

                    if i == "Child":
                        NewName = self.Child(j)

                    if i =="Parent":
                        NewName=self.Parent(j)
                    if i == "Grandparent":
                        NewName =self.GrandParent(j)

                    shutil.copy(j,NewName)
                    Names.append(NewName)
                if i =="Child":
                    Data["Parent"] = Names
                if i == "Parent":
                    Data["Grandparent"] = Names
                if i =="Grandparent":
                    Data[today] = Names
                Names = []
            with open(FileName,"w")as fp:
                json.dump(Data,fp)

        def Child(self,FileName):
            SplitName = FileName.split(".")
            SplitName.insert(1,"-Parent")
            NewName = SplitName[0]+ SplitName[1]+ "."+SplitName[2]
            return NewName


        def Parent(self,FileName):
            SplitName = FileName.split(".")
            DoubleSplitName = []
            for i in SplitName:
                DoubleSplitName.append(i.split("-"))
            DoubleSplitName[0][1] = "-GrandParent"
            NewName = str(DoubleSplitName[0][0])+ str(DoubleSplitName[0][1])+"."+ str(DoubleSplitName[1][0])
            return NewName

        def GrandParent(self,FileName):
            SplitName = FileName.split(".")
            DoubleSplitName = []
            for i in SplitName:
                DoubleSplitName.append(i.split("-"))
            date =datetime.datetime.today()
            dateFormate =  datetime.datetime.strftime(date,"-%d%B%Y-%H:%M")
            DoubleSplitName[0][1] = dateFormate
            NewName = str(DoubleSplitName[0][0])+ str(DoubleSplitName[0][1])+"."+ str(DoubleSplitName[1][0])
            return NewName

        def RecoveryName(self,FileName):

                SplitName = FileName.split(".")
                DoubleSplitName = []
                for i in SplitName:
                    DoubleSplitName.append(i.split("-"))
                NewName = str(DoubleSplitName[0][0])+"."+ str(DoubleSplitName[1][0])
                return NewName


        def RecoverBackUp(self,FileName):
            with open(FileName)as fp:
                Data = json.load(fp)

            AnchorValue = self.PastBackupsList.get(tk.ANCHOR)

            if AnchorValue !="Child" and AnchorValue !="":

                Names = []
                for i in Data[AnchorValue]:

                    NewName = self.RecoveryName(i)
                    shutil.copy(i,NewName)
                    Names.append(NewName)

                Data["Child"] = Names

                Names = []
                with open(FileName,"w")as fp:
                    json.dump(Data,fp)




