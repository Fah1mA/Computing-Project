from tkinter import *


def GUI():
    form = Tk()
    form.geometry("600x320")

    titleLabel = Label(form, text="Main Menu")
    titleLabel.config(font=("Courier", 15))
    titleLabel.grid(row=0, column=1, columnspan=3, sticky="N", padx=200, pady=10)

    exitButton = Button(form, text="Exit", width=12, command=quit)
    exitButton.grid(row=3, column=0)

    loginButton = Button(form, text="Login", width=12, command=lambda: login(form))
    loginButton.grid(row=3, column=1)

    def login(f):
        login = Tk()
        login.geometry("600x320")

        userLabel = Label(login, text="Username")
        userLabel.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        passwordLabel = Label(login, text="Password")
        passwordLabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        userEntry = Entry(login, width="30")
        userEntry.grid(row=1, column=1, padx=10, pady=10, sticky="E")
        passwordEntry = Entry(login, width="30")
        passwordEntry.grid(row=2, column=1, padx=10, pady=10, sticky="E")

        backButton = Button(login, text="Back", width=12, command=lambda: [dlogin(login)])
        backButton.grid(row=3, column=0)

        enterButton = Button(login, text="Enter", width=12)
        enterButton.grid(row=4, column=2, padx=200, pady=150)
        userEntry.focus()
        return

    def dlogin(login):
        login.destroy()


#=================================================================
# Start with a page with a login button and a cancel button.
# The login button should take you to a menu.
# The login page can also have away for the admin to login.
# It should include a simple password
# The when a user logs in they should change there password.
#=================================================================
# The page should also have a cancel button.
# It should make the user exit the page.
#=================================================================
# when logged in table should show
# allow user to customize


if __name__ == "__main__":
    GUI()
