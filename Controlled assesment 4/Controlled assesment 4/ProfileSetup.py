import json
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from Gui import *
import Config

class ProfileSetup(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.BackButton= tk.Button(self, text="Back",command=self.BackButtonRun)


        self.lblFirstName= tk.Label(self,text=" First Name :")
        self.lblLastName= tk.Label(self,text=" Last Name :")
        self.lblPhoneNumber= tk.Label(self,text=" Phone Number :")
        self.lblAddress= tk.Label(self,text=" Address :")
        self.lblPostcode= tk.Label(self,text=" Postcode :")
        self.lblDateOfBirth= tk.Label(self,text=" Date of Birth :")
        self.txtFirstName = ttk.Entry(self)
        self.txtLastName = ttk.Entry(self)
        self.txtPhoneNumber = ttk.Entry(self)
        self.txtAddress = ttk.Entry(self)
        self.txtPostcode = ttk.Entry(self)
        self.txtDateOfBirth = ttk.Entry(self)


        self.SubmitButton= tk.Button(self, text="Submit",command=lambda: self.addNewPlayer(controller) )
        self.BackButton= tk.Button(self, text="Back",command=lambda: controller.show_frame("Login"))

        self.lblFirstName.grid(row=1,column=0)
        self.lblLastName.grid(row=2,column=0)
        self.lblPhoneNumber.grid(row=3,column=0)
        self.lblAddress.grid(row=4,column=0)
        self.lblPostcode.grid(row=5,column=0)
        self.lblDateOfBirth.grid(row=6,column=0)
        self.txtFirstName.grid(row=1,column=1)
        self.txtLastName.grid(row=2,column=1)
        self.txtPhoneNumber.grid(row=3,column=1)
        self.txtAddress.grid(row=4,column=1)
        self.txtPostcode.grid(row=5,column=1)
        self.txtDateOfBirth.grid(row=6,column=1)
        self.SubmitButton.grid(row=8,column=0,columnspan=2)
        self.BackButton.grid(row=9,column = 0,columnspan = 2)

    def BackButtonRun(self):
        global PagesViewed
        PagesViewed.pop()
        controller.show_frame(PagesViewed[-1])


    def getPlayerData(self):
        firstName = self.txtFirstName.get()
        lastName = self.txtLastName.get()
        phoneNumber = self.txtPhoneNumber.get()
        address = self.txtAddress.get()
        postCode = self.txtPostcode.get()
        DOB = self.txtDateOfBirth.get()



        return firstName , lastName, phoneNumber, address, postCode, DOB

    def addNewPlayer(self,controller):
        global CurrentUser
        firstName , lastName, phoneNumber, address, postCode, DOB = self.getPlayerData()

        data = {}
        players={}

        if self.validPlayerData(firstName , lastName, phoneNumber, address, postCode, DOB) == True :


            with open('players.json', 'r') as fp:
                    players = json.load(fp)
            data["First name"] = firstName
            data["Last name"] = lastName
            data["Phone number"] = phoneNumber
            data["Address"] = address
            data["Post code"] = postCode
            data["Date of Birth"] =DOB
            players[Config.CurrentUser] = data


            with open('players.json', 'w+') as fp:
                    json.dump(players, fp)

            controller.show_frame("Home")

    def validPlayerData(self,firstName,lastName,phoneNumber,Address,Postcode,dateOfBirth):
        valid = [self.validFirstName(firstName)
        ,self.validLastName(lastName)
        ,self.validPhoneNumber(phoneNumber)
        ,self.validAddress(Address)
        ,self.validPostcode(Postcode)
        ,self.validDateOfBirth(dateOfBirth)]
        for i in valid:
            if i == False :
                return False
        return True

    def validFirstName(self,firstName):
        if len(firstName) <30:
            return True
        else:
            messagebox.showinfo("",firstName +" is not a valid first name.")
            return False
    def validLastName(self,LastName):
        if len(LastName) <30:
            return True
        else:
            messagebox.showinfo("",LastName +" is not a valid Last name.")
            return False

    def validPhoneNumber(self,phoneNumber):
        if phoneNumber.isdigit() == True:
            if phoneNumber[0] == "0" :
                if len(phoneNumber) == 11 :
                    return True
        messagebox.showinfo("",phoneNumber +" is not a valid phone number.")
        return False
    def validAddress(self,address):
        if len(address) < 30:
            return True
        messagebox.showinfo("",address +" is not a valid address.")
        return False
    def validPostcode(self,postcode):

##        if re.match("^(([gG][iI][rR] {0,}0[aA]{2})|((([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y]?[0-9][0-9]?)|(([a-pr-uwyzA-PR-UWYZ][0-9][a-hjkstuwA-HJKSTUW])|([a-pr-uwyzA-PR-UWYZ][a-hk-yA-HK-Y][0-9][abehmnprv-yABEHMNPRV-Y]))) {0,}[0-9][abd-hjlnp-uw-zABD-HJLNP-UW-Z]{2}))$)",postcode) == False:
            return True
##          messagebox.showinfo(postcode +" is not a valid postcode.")
##        return False

    def validDateOfBirth(self,dateOfBirth):
##        try:
##            datetime.strptime(dateOfBirth, '%d/%m/%Y')
##        except ValueError:
##            messagebox.showinfo("",dateOfBirth +" is not a valid date of birth.")
##            return False
##        if datetime.now() - timedelta(days=2000) > datetime.strptime(dateOfBirth, '%d/%m/%Y'):
##            return True
##        messagebox.showinfo("",dateOfBirth +" is not a valid date of birth.")
##        return False
        return True
