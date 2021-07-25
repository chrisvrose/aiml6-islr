from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from PIL import Image
from tkinter import messagebox
from creating_dataset import cd_main
from Prediction import pred_main
from Reverse_Recognition import rr_main

#global variables
bg=None
selection=1


# =====================Create Database=============================================
def createdb():
    conn = sqlite3.connect('files/users_info.db')
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS users (name TEXT , passs TEXT,sqltime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL)")
    conn.commit()
    conn.close()


createdb()


# ======================Adding new user in database===============================
def saveadmin():
    name_err = name_entry.get()
    pass_err = pass_entry.get()
    if name_err == "":
        messagebox.showinfo("Invalid input", "Username can't be Empty")
    elif pass_err == "":
        messagebox.showinfo("Invalid input", "Password can't be Empty")
    else:
        conn = sqlite3.connect("files/users_info.db")
        c = conn.cursor()
        c.execute("INSERT INTO users(name,passs) VALUES(?,?) ", (name_entry.get(), pass_entry.get()))
        conn.commit()
        messagebox.showinfo("Information", "New User has been Added")


# ========================Fetching data of user from database==========================
def loggin():
    while True:
        a = name2_entry.get()
        b = pass2_entry.get()
        with sqlite3.connect("files/users_info.db") as db:
            cursor = db.cursor()
        find_user = ("SELECT * FROM users WHERE name = ? AND passs = ?")
        cursor.execute(find_user, [(a), (b)])
        results = cursor.fetchall()
        if results:
            for i in results:
                window.destroy()
                # ==================Window2+CreateFrame+Animation============================================================
                window2 = Tk()
                f1 = Frame(window2)
                f2 = Frame(window2)
                f3 = Frame(window2)
                f4 = Frame(window2)

                def swap(frame):
                    frame.tkraise()

                for frame in (f1, f2, f3, f4):
                    frame.place(x=0, y=0, width=400, height=400)
                window2.geometry("400x400+420+170")
                window2.resizable(False, False)
                label3 = Label(f1, text="User Panel", font=("arial", 20, "bold"), bg="grey16", fg="white",
                               relief=SUNKEN)
                label3.pack(side=TOP, fill=X)

                label4 = Label(f2, text="                            Indian Sign Language Recognition System", font=("arial", 10, "bold"), bg="grey16",
                               fg="white")
                label4.pack(side=BOTTOM, fill=X)
                statusbar = Label(f1, text="                            Indian Sign Language Recognition System", font=("arial", 8, "bold"),
                                  bg="grey16", fg="white", relief=SUNKEN, anchor=W)
                statusbar.pack(side=BOTTOM, fill=X)


                label4 = Label(f3, text="                            Indian Sign Language Recognition System", font=("arial", 10, "bold"), bg="grey16",
                               fg="white")
                label4.pack(side=BOTTOM, fill=X)

                # =========================Main Buttons=========================================

                btn2w2 = ttk.Button(f1, text="Predict Sign", command=pred_main)
                btn2w2.place(x=255, y=115, width=150, height=30)

                btn3w2 = ttk.Button(f1, text="Translate speech", command=rr_main)
                btn3w2.place(x=255, y=170, width=150, height=30)

                btn6w2 = ttk.Button(f1, text="Create Signs", command=cd_main)
                btn6w2.place(x=255, y=225, width=150, height=30)

                # =========================Developers Page=========================================

                label10 = Label(f4, text="", font=("arial", 20, "bold"), bg="grey16", fg="white")
                label10.pack(side=TOP, fill=X)
                label11 = Label(f4, text="     Indian Sign Language Recognition System", font=("arial", 10, "bold"), bg="grey16",
                                fg="white")
                label11.pack(side=BOTTOM, fill=X)

                label10 = Label(f4, text=" Information Will be Added Soon!", font=("arial", 12, "bold"))
                label10.place(x=75, y=150)

                def swap4(frame):
                    frame.tkraise()
                    statusbar['text'] = '                            Indian Sign Language Recognition System'

                btn4w2 = ttk.Button(f4, text="Back	", command=lambda: swap4(f1))
                btn4w2.place(x=3, y=40, width=50, height=30)

                def swap3(frame):
                    frame.tkraise()

                btn9w2 = ttk.Button(f1, text="Developers", command=lambda: swap3(f4))
                btn9w2.place(x=255, y=280, width=150, height=30)

                def quit():
                    window2.destroy()

                btn9w2 = ttk.Button(f1, text="Exit", command=quit)
                btn9w2.place(x=255, y=335, width=150, height=30)

                f1.tkraise()
                window2.mainloop()

            break
        else:
            messagebox.showerror("Error", "invalid username or password")
            break


# ======================Main Login Screen============================================

window = Tk()
window.title("Login Panel")
Label1 = Label(window, text="Login Panel", font=("arial", 20, "bold"), bg="grey19", fg="white")
Label1.pack(side=TOP, fill=X)
Label2 = Label(window, text="", font=("arial", 10, "bold"), bg="grey19", fg="white")
Label2.pack(side=BOTTOM, fill=X)

# ====================Login and Signup Tabs====================================

nb = ttk.Notebook(window)
tab1 = ttk.Frame(nb)
tab2 = ttk.Frame(nb)
nb.add(tab1, text="Login")
nb.add(tab2, text="Sign_up")
nb.pack(expand=True, fill="both")

# =============Login tab=========================================

name2_label = Label(tab1, text="Name", font=("arial", 10, "bold"))
name2_label.place(x=10, y=10)
name2_entry = StringVar()
name2_entry = ttk.Entry(tab1, textvariable=name2_entry)
name2_entry.place(x=90, y=10)
name2_entry.focus()

pass2_label = Label(tab1, text="Password", font=("arial", 10, "bold"))
pass2_label.place(x=10, y=40)
pass2_entry = StringVar()
pass2_entry = ttk.Entry(tab1, textvariable=pass2_entry, show="*")
pass2_entry.place(x=90, y=40)

# =====================Signup Tab===============================
name_label = Label(tab2, text="Name", font=("arial", 10, "bold"))
name_label.place(x=10, y=10)
name_entry = StringVar()
name_entry = ttk.Entry(tab2, textvariable=name_entry)
name_entry.place(x=90, y=10)
name_entry.focus()
pass_label = Label(tab2, text="Password", font=("arial", 10, "bold"))
pass_label.place(x=10, y=40)
pass_entry = StringVar()
pass_entry = ttk.Entry(tab2, textvariable=pass_entry, show="*")
pass_entry.place(x=90, y=40)


def clear():
    name_entry.delete(0, END)
    pass_entry.delete(0, END)

# ===============User Buttons==============================================

btn1 = ttk.Button(tab2, text="Add User", command=saveadmin)
btn1.place(x=50, y=80)
btn2 = ttk.Button(tab2, text="Clear", command=clear)
btn2.place(x=140, y=80)

# ================Login Button Main======================================

btn3 = ttk.Button(tab1, text="Login", width=20, command=loggin)
btn3.place(x=87, y=80)

window.geometry("400x400+420+170")
window.resizable(False, False)
window.mainloop()
