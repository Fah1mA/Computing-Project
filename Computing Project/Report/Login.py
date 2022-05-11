from tkinter import *


def GUI():
    form = Tk()
    form.geometry("600x320")

    titleLabel = Label(form, text="Main Menu")
    titleLabel.config(font=("Courier", 15))
    titleLabel.grid(row=0, column = 1, columnspan= 3, sticky = "N", padx= 200, pady = 10)

    exitButton = Button(form, text= "Exit",width = 12, command = quit)
    exitButton.grid(row = 3, column = 0)


    loginButton = Button(form, text="Login", width = 12, command=lambda:login(form))
    loginButton.grid(row=3, column = 1)

    signinButton = Button(form, text="Sign In", width = 12, command=lambda:signin(form))
    signinButton.grid(row=3, column = 2)
    

    
    def signin(f):
        sign = Tk()
        sign.geometry("600x320")

        userLabel = Label(sign, text="Username")
        userLabel.grid(row=1, column=0, sticky="W")
        passwordLabel = Label(sign, text="Password")
        passwordLabel.grid(row=2, column=0, sticky="W")
        repasswordLabel = Label(sign, text="Re-Password")
        repasswordLabel.grid(row=3, column=0, sticky="W")


        userEntry = Entry(sign, width = "30")
        userEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")
        passwordEntry = Entry(sign, width = "30")
        passwordEntry.grid(row=2, column = 1,padx=10, pady=10, sticky="E")
        repasswordEntry = Entry(sign, width = "30")
        repasswordEntry.grid(row=3, column = 1,padx=10, pady=10, sticky="E") 


        backButton = Button(sign, text="Back", width = 12, command=lambda:[dsignin(sign)])
        backButton.grid(row = 4, column=0)

        enterButton = Button(sign, text="Enter", width = 12, command=lambda:login(f))
        enterButton.grid(row=4, column = 2, padx=200, pady=150)

        userEntry.focus()
        return

    def dsignin(sign):
        sign.destroy()
    
    def login(f):
        login=Tk()
        login.geometry("600x320")

        userLabel = Label(login, text="Username")
        userLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        passwordLabel = Label(login, text="Password")
        passwordLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        userEntry = Entry(login, width = "30")
        userEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")
        passwordEntry = Entry(login, width = "30")
        passwordEntry.grid(row=2, column = 1, padx=10, pady=10, sticky="E")

        backButton = Button(login, text="Back", width = 12, command=lambda:[dlogin(login)])
        backButton.grid(row = 3, column=0)

        enterButton = Button(login, text="Enter", width = 12)
        enterButton.grid(row=4, column = 2, padx=200, pady=150)
        userEntry.focus()
        return

    def dlogin(login):
        login.destroy()



     
GUI()
