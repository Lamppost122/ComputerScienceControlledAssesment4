import json
import hashlib
import imaplib
import email
import tkinter as tk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import ttk
from SystemToolKit import *

class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.Title = ttk.Label(self, text="Please login to your account", font=controller.title_font).grid(row=0,column=0,columnspan=2)
        self.loginButton = ttk.Button(self, text="Login",command= lambda:self.checkDetails(controller))
        self.loginButton.grid(row=4,column=1)
        self.registerButton = ttk.Button(self, text="Register",command=lambda: controller.show_frame("Register")).grid(row=4,column=0)
        self.lblUsername = ttk.Label(self,text="Username: ").grid(row=1,column=0)
        self.lblPassword = ttk.Label(self,text="Password: ").grid(row=2,column=0)
        self.txtUsername = ttk.Entry(self)
        self.txtUsername.grid(row=1,column = 1)
        self.txtPassword = ttk.Entry(self)
        self.txtPassword.grid(row=2,column = 1)

    def checkDetails(self,controller):
        global CurrentUser, AccessLevel
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        users = SystemToolKit.readFile("data.json")




        for j,i in enumerate(users):
            userHash = users[i]["Password"]
            salt = users[i]["Salt"]
            if self.checkPassword(userHash,password,salt) == True:
                CurrentUser = i
                if users[i]["ValidEmail"] == True :

                    AccessLevel = users[i]["AccessLevel"]
                    controller.show_frame("Home")
                    break
                else :

                    self.ValidateEmail(CurrentUser)

                    if users[i]["ValidEmail"] == True :

                        AccessLevel = users[i]["AccessLevel"]
                        controller.show_frame("ProfileSetup")
                        break
                    else :
                        messagebox.showinfo("Messgae","You need to confirm your email")
                        break

            elif (j+1) == len(users):

                messagebox.showinfo("Messgae","Username or password incorrect")
        if len(users) == 0:
            messagebox.showinfo("Messgae","No users installed")

    @staticmethod
    def checkPassword(userHash,password,salt):
        if userHash  == hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest():
            return True
        else:
            return False


    def ValidateEmail(self,UserID):
        with open('data.json', 'r') as fp:
                users = json.load(fp)
        self.read_Email()

##        if responce == True :
##
##            users[userID]["ValidEmail"] = True
##            with open('data.json', 'w+') as fp:
##                json.dump(users, fp)


    def read_Email(self):
            ORG_EMAIL   = "@gmail.com"
            FROM_EMAIL  = "ComputerScienceTest1" + ORG_EMAIL
            FROM_PWD    = "Password1@"
            SMTP_SERVER = "imap.gmail.com"
            SMTP_PORT   = 993
            mail = imaplib.IMAP4_SSL(SMTP_SERVER)
            mail.login(FROM_EMAIL,FROM_PWD)
            mail.select('inbox')

            type, data = mail.search(None, 'ALL')
            mail_ids = data[0]

            id_list = mail_ids.split()
            first_email_id = int(id_list[0])
            latest_email_id = int(id_list[-1])

            inbox = []

            for i in range(latest_email_id,first_email_id, -1):
                typ, data = mail.fetch(i, '(RFC822)' )

                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        email_subject = msg['subject']
                        Emails =email_subject.split("|")
                        print Emails
                        Data = {Emails[1]:Emails[0]}
                        inbox.append(Data)


            print(inbox)
            return inbox


