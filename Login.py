from tkinter import *
import customtkinter as ttk
from firebase import Username, Password

page = ttk.CTk()
page.title("Login")
x = page.winfo_screenwidth() // 6
y = page.winfo_screenheight() * 0.15
page.geometry(f"950x600+{x}+{y}")
page.wm_iconbitmap("assets/login_icon.ico")
page.resizable(False, False)
page.propagate()

load_img = PhotoImage(file="assets/login.png")
img = load_img.subsample(2, 2)
Label(page, image=load_img, width=700).pack(side=LEFT, fill=Y)


def userFunc(e):
    if userName.get() != "":
        pass
    else:
        userName.insert(0, "Enter User Name")


def passwordFunc(e):
    if password.get() != "":
        pass
    else:
        password.insert(0, "Enter Password")


frame = ttk.CTkFrame(page)
ttk.CTkLabel(frame, text="LOGIN", font=("", 45, "bold")).pack(fill=BOTH, pady=40)
userName = ttk.CTkEntry(frame, width=350, height=45)
userName.pack(pady=5, padx=42)
userName.insert(0, "Enter User Name")
userName.bind("<FocusIn>", lambda e: userName.delete(0, 'end'))
userName.bind("<FocusOut>", userFunc)
password = ttk.CTkEntry(frame, width=350, height=45)
password.pack(pady=5, padx=42)
password.insert(0, "Enter Password")
password.bind("<FocusIn>", lambda e: password.delete(0, 'end'))
password.bind("<FocusOut>", passwordFunc)


def Login():
    if userName.get() == Username and int(password.get()) == Password:
        print("logged in")
        userName.insert(0, "Enter User Name")
        password.insert(0, "Enter Password")
    elif userName.get() == Username and int(password.get()) != Password:
        print("incorrect password")
    elif userName.get() != Username and int(password.get()) == Password:
        print("incorrect user name")
    elif userName.get() != Username and int(password.get()) != Password:
        print("incorrect user name and password")


loginButton = ttk.CTkButton(frame, text="Login", width=350, height=45, font=("", 28, "bold"), command=Login)
loginButton.pack(pady=20)

ttk.CTkLabel(frame, text="Others").pack()

load_google = PhotoImage(file='assets/google_logo.png')
google = load_google.subsample(2, 2)
load_github = PhotoImage(file='assets/github_logo.png')
github = load_github.subsample(2, 2)

google_Button = ttk.CTkButton(frame, image=google, text="Goggle", width=350, height=45, font=("", 28, "bold"),
                              fg_color="white", text_color="black")
google_Button.pack(pady=20)
github_Button = ttk.CTkButton(frame, image=github, text="Git Hub", width=350, height=45, font=("", 28, "bold"),
                              fg_color="white", text_color="black")
github_Button.pack()

frame.pack(side=RIGHT, fill=Y, pady=20, padx=20)
page.mainloop()
