from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import ImageTk


def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)


def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get == '':
        messagebox.showerror('Error', 'All Fields Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Not Match')

    elif check.get() == 0:
        messagebox.showerror('Error', 'Please Accept Terms & Conditions')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connection Error Please Try Again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null, email varchar(25), username varchar(30),password varchar(8))'
            mycursor.execute(query)

        except:
            mycursor.execute('use userdata')

        query = 'select * from data where username=%s'
        mycursor.execute(query, (usernameEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username Already Exist')
        else:
            query = 'insert into data(email,username,password) values (%s,%s,%s)'
            mycursor.execute(query, (emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success', 'Registration is Successful')
            signup_window.destroy()


def login():
    signup_window.destroy()


signup_window = Tk()
signup_window.geometry()
signup_window.resizable(0, 0)
signup_window.title("Signup Page")

bgImage = ImageTk.PhotoImage(file='images.jpeg')

bgLabel = Label(signup_window, image=bgImage)
bgLabel.grid(row=0, column=0)

frame = Frame(signup_window, bg='white')
frame.place(x=350, y=30)

heading = Label(frame, text="CRATE AN ACCOUNT", bg='white', font=('roboto', 13, 'bold'), fg='dark turquoise')
heading.grid()

# email

email = Label(frame, text="Email", bg='white', font=('roboto', 10, 'bold'), fg='dark turquoise')
email.grid(row=1, sticky='w', padx=25, pady=(5, 0))

emailEntry = Entry(frame, width=28, fg='white', font=('roboto', 11, 'bold'), bg='dark turquoise')
emailEntry.grid(row=2, sticky='w', padx=25)

# username

username = Label(frame, text="Username", bg='white', font=('roboto', 10, 'bold'), fg='dark turquoise')
username.grid(row=3, sticky='w', padx=25, pady=(5, 0))

usernameEntry = Entry(frame, width=28, fg='white', font=('roboto', 11, 'bold'), bg='dark turquoise')
usernameEntry.grid(row=4, sticky='w', padx=25)

# password
password = Label(frame, text="Password", bg='white', font=('roboto', 10, 'bold'), fg='dark turquoise')
password.grid(row=5, sticky='w', padx=25, pady=(5, 0))

passwordEntry = Entry(frame, width=28, fg='white', font=('roboto', 11, 'bold'), bg='dark turquoise')
passwordEntry.grid(row=6, sticky='w', padx=25)

# confirm password

confirm = Label(frame, text="Confirm Password", bg='white', font=('roboto', 10, 'bold'), fg='dark turquoise')
confirm.grid(row=7, sticky='w', padx=25, pady=(5, 0))

confirmEntry = Entry(frame, width=28, fg='white', font=('roboto', 11, 'bold'), bg='dark turquoise')
confirmEntry.grid(row=8, sticky='w', padx=25)

# term and condition

check = IntVar()

terms = Checkbutton(frame, text='I agree to the Term & Conditions', fg='dark turquoise', font=('roboto', 10, 'bold'),
                    bg='white', activebackground='white', activeforeground='dark turquoise', cursor='hand2',
                    variable=check)
terms.grid(row=9, padx=15, pady=5)

# Button
createButton = Button(frame, text='Create', fg='white', font=('roboto', 10, 'bold'), bg='lime green',
                      activebackground='white', activeforeground='dark turquoise', width=29,
                      command=connect_database)
createButton.grid(row=10, pady=5)

account = Label(frame, text='I have an account!', font=('roboto', 10, 'bold'), bg='white', fg='dark turquoise')
account.grid(row=11, sticky='w', pady=(5, 20), padx=25)

sign_in = Button(frame, width=12, text='Login Page', bg='white', bd=0, cursor='hand2', fg='Royalblue1',
                 font=('roboto', 10, 'bold underline'),
                 command=login)
sign_in.place(x=155, y=298)

signup_window.mainloop()
