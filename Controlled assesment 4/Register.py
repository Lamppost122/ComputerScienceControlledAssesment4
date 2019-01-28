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




class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.Title = tk.Label(self, text="Please fill in your details", font=controller.title_font)
        self.loginButton = ttk.Button(self, text="Login",command=lambda: controller.show_frame("Login") )
        self.registerButton = ttk.Button(self, text="Register",command=lambda: self.register())
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

        self.cmbAccessLevel = ttk.OptionMenu(self, self.var,*options)


        self.txtUsername.grid(row=1,column = 1)
        self.txtConfirmUsername.grid(row=2,column = 1)
        self.txtPassword.grid(row=3,column = 1)
        self.txtConfirmPassword.grid(row=4,column = 1)
        self.txtEmail.grid(row=5,column = 1)
        self.loginButton.grid(row=7,column = 1)
        self.registerButton.grid(row=7,column = 0)
        self.lblUsername.grid(row=1,column = 0)
        self.lblConfirmUsername.grid(row=2,column = 0)
        self.lblPassword.grid(row=3,column = 0)
        self.lblConfirmPassword.grid(row=4,column = 0)
        self.lblEmail.grid(row=5,column = 0)
        self.Title.grid(row=0,column = 0,columnspan=2)
        self.lblAccessLevel.grid(row=6,column =0 )
        self.cmbAccessLevel.grid(row=6,column = 1)

    def register(self):
        username, password, confirmUsername, confirmPassword, Email, AccessLevel, ValidEmail = self.getRegisterData()
        self.addNewUser(username, password, confirmUsername, confirmPassword, Email, AccessLevel, ValidEmail)
        self.sendEmailConformation(Email)


    def getRegisterData(self):

        username =  self.txtUsername.get()
        confirmUsername = self.txtConfirmUsername.get()
        password = self.txtPassword.get()
        confirmPassword = self.txtConfirmPassword.get()
        Email = self.txtEmail.get()
        accessLevel = self.var.get()
        ValidEmail = False


        return username, password, confirmUsername, confirmPassword, Email, accessLevel, ValidEmail

    def addNewUser(self,username, password, confirmUsername, confirmPassword, Email, accessLevel, ValidEmail):

        data = {}
        users={}

        if username == confirmUsername and password == confirmPassword :

            users = SystemToolKit.readFile("data.json")
            salt = uuid.uuid4().hex
            hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
            userID = str(uuid.uuid4())
            data["Username"] = username
            data["Password"] = hashed_password
            data["Salt"] = salt
            data["Email"] = Email
            data["AccessLevel"] = accessLevel
            data["ValidEmail"] = ValidEmail
            users[userID] = data
            with open('data.json', 'w+') as fp:
                json.dump(users, fp)


    def sendEmailConformation(self,email):

        msg = MIMEMultipart()
        text = "Did you register for a account ?"
        body = text
        body = text + """\
        <html>
        <head></head>
        <body>
        <code></code>
        <form id = "gform" method = "POST" action = "https://script.google.com/macros/s/https://script.google.com/macros/s/AKfycby_l5o0B1H1GfSXLa0sIY2qdzR32p_U7Q_VwOm6C_bkK1AXnf4/exec" >
        <input type="radio" name="Button" value="Yes """+"|" +str(email)+ """"  checked> Yes<br>
        <input type="radio" name="Button" value="No  """+"|"+str(email) +""""> No<br>
        <input type="submit" value="Submit">

        </body>
        </html>
        """
        msg['Subject'] = "Comfirm email"
        msg.attach(MIMEText(body, 'html'))
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("ComputerScienceTest1@gmail.com", "Password1@")
        server.sendmail("ComputerScienceTest1@gmail.com", email, text)
        server.quit()


