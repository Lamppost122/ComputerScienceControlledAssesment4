import tkinter as tk
import json
import smtplib
import uuid
import hashlib
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import  messagebox
from tkinter import ttk
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from SystemToolKit import *
from Gui import *
import random





class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.Title = tk.Label(self, text="Please fill in your details", font=controller.title_font)
        self.loginButton = tk.Button(self, text="Login",command=lambda: controller.show_frame("Login") )
        self.registerButton = tk.Button(self, text="Register",command=lambda: self.register(controller))
        self.lblUsername = ttk.Label(self,text="Username: ")
        self.lblPassword = ttk.Label(self,text="Password: ")
        self.lblConfirmUsername = ttk.Label(self,text="Confirm Username: ")
        self.lblConfirmPassword = ttk.Label(self,text="Confirm Password: ")
        self.lblEmail = ttk.Label(self,text="Email: ")
        self.txtUsername = ttk.Entry(self)
        self.txtConfirmUsername = ttk.Entry(self)
        self.txtPassword = ttk.Entry(self)
        self.txtConfirmPassword = ttk.Entry(self)
        self.txtEmail = ttk.Entry(self)
        self.lblAccessLevel = ttk.Label(self,text = "Position: ")
        self.var = tk.StringVar()
        options = ["Player","Coach/Captin","Admin"]
        self.var.set(options[0])

        self.cmbAccessLevel = tk.OptionMenu(self, self.var,*options)

        self.Title.config(background="#f4f8ff",fg = "#485e82",pady="5")
        self.txtPassword.config(width="20",show="*")
        self.txtConfirmPassword.config(width="20",show="*")


        self.txtUsername.grid(row=1,column = 1)
        self.txtConfirmUsername.grid(row=2,column = 1)
        self.txtPassword.grid(row=3,column = 1)
        self.txtConfirmPassword.grid(row=4,column = 1)
        self.txtEmail.grid(row=5,column = 1)
        self.loginButton.grid(row=7,column = 0)
        self.registerButton.grid(row=7,column = 1)
        self.lblUsername.grid(row=1,column = 0)
        self.lblConfirmUsername.grid(row=2,column = 0)
        self.lblPassword.grid(row=3,column = 0)
        self.lblConfirmPassword.grid(row=4,column = 0)
        self.lblEmail.grid(row=5,column = 0)
        self.Title.grid(row=0,column = 0,columnspan=2)
        self.lblAccessLevel.grid(row=6,column =0 )
        self.cmbAccessLevel.grid(row=6,column = 1)

    def register(self,controller):
        self.getRegisterData()
        self.addNewUser()
        self.sendEmailConformation()
        messagebox.showinfo("Messgae","Thank you for registring with us. You will need to confirm your email")
        controller.show_frame("Login")


    def getRegisterData(self):

        self.username =  self.txtUsername.get()
        self.confirmUsername = self.txtConfirmUsername.get()
        self.password = self.txtPassword.get()
        self.confirmPassword = self.txtConfirmPassword.get()
        self.Email = self.txtEmail.get()
        self.accessLevel = self.var.get()
        self.ValidEmail = False
        self.confirmationCode = str(random.randint(10000,99999))



    def addNewUser(self):

        data = {}
        users={}

        if self.username == self.confirmUsername and self.password == self.confirmPassword :

            users = SystemToolKit.readFile("data.json")
            salt = uuid.uuid4().hex
            hashed_password = hashlib.sha512(self.password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
            userID = str(uuid.uuid4())
            data["Username"] = self.username
            data["Password"] = hashed_password
            data["Salt"] = salt
            data["Email"] = self.Email
            data["AccessLevel"] = self.accessLevel
            data["ValidEmail"] = self.ValidEmail
            data["Confirmation code"] = self.confirmationCode
            users[userID] = data
            with open('data.json', 'w+') as fp:
                json.dump(users, fp)



    def sendEmailConformation(self):

        msg = MIMEMultipart()
        text = "Confirmation code: "
        body = text + self.confirmationCode
        msg['Subject'] = "Comfirm email"
        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("ComputerScienceTest1@gmail.com", "Password1@")
        server.sendmail("ComputerScienceTest1@gmail.com", self.Email, text)
        server.quit()


