import datetime
import os
import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
import uuid
from MatchScreen import *

class ImportData(tk.Frame):

        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            self.Title = tk.Label(self,text="Import Data",font= controller.title_font)
            self.txtFileName =tk.Entry(self)
            self.importButton =tk.Button(self,text ="Import")


        def ImportData(FileName,DataFileName):
            with open(DataFileName)as fp:
                FileData=json.load(fp)
            with open(FileName)as fp:
                File=fp.readlines()



            delimiter = ","
            TeamNumber= 0
            for i ,j in enumerate(File):

                if i==0:
                    HeaderRow = j.split(delimiter)
                    for m,n in enumerate(HeaderRow):
                        if n.lower() == "team":
                            TeamNumber = m +1


                    #Validate Header types
                else:
                    rowData = j.split(delimiter)
                    Data={}
                    TeamData = {}
                    for k,l in enumerate(rowData):
                        if k ==TeamNumber:
                            TeamID = MatchScreen.GetTeamID(TeamNumber)
                        else:

                            Data[HeaderRow[k]]= l
                    TeamData[str(uuid.uuid4())] = Data

                    FileData[TeamID] = TeamData
            with open(FileName,"w")as fp:
                 json.dump(FileData,fp)

