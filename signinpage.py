from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import ImageTk


def forgot_pass():
    def change_password():
        if usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
            messagebox.showerror("Error", "All Fields Are Empty", parent=window)
        elif passwordEntry.get() != confirmEntry.get():
            messagebox.showerror("Error", "Password and Confirm Password are not match", parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='1', database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, user.get())
            row = mycursor.fetchone()
            if row != None:
                messagebox.showerror('Error', 'Invalid Username', parent=window)
            else:
                query = 'update data set password=%s where username=%s'
                mycursor.execute(query, (confirmEntry.get(), usernameEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('success', 'password is reset,please login with new password', parent=window)
                window.destroy()

    window = Toplevel()
    window.title('Change Password')

    bgImage = ImageTk.PhotoImage(file='images.jpeg')
    bgLabel = Label(window, image=bgImage)
    bgLabel.grid(row=0, column=0)

    frame = Frame(window, bg='white')
    frame.place(x=350, y=30)

    heading = Label(frame, text="RESET PASSWORD", bg='white', font=('roboto', 18, 'bold'), fg='dark turquoise')
    heading.grid()

    # username

    username = Label(frame, text="Username", bg='white', font=('roboto', 12, 'bold'), fg='dark turquoise')
    username.grid(row=1, sticky='w', padx=15, pady=(10, 2))

    usernameEntry = Entry(frame, width=20, fg='dark turquoise', font=('roboto', 12, 'bold'), bd=0)
    usernameEntry.grid(row=2, sticky='w', padx=15, )
    Frame(frame, width=200, height=2, bg='dark turquoise').grid(row=3, sticky='w', padx=20)

    # password
    password = Label(frame, text=" New Password", bg='white', font=('roboto', 12, 'bold'), fg='dark turquoise')
    password.grid(row=4, sticky='w', padx=15, pady=(10, 0))

    passwordEntry = Entry(frame, width=20, fg='dark turquoise', font=('roboto', 12, 'bold'), bd=0)
    passwordEntry.grid(row=5, sticky='w', padx=15, )
    Frame(frame, width=200, height=2, bg='dark turquoise').grid(row=6, sticky='w', padx=20)
    # confirm password

    confirm = Label(frame, text="Confirm Password", bg='white', font=('roboto', 12, 'bold'), fg='dark turquoise')
    confirm.grid(row=7, sticky='w', padx=15, pady=(10, 0))

    confirmEntry = Entry(frame, width=20, fg='dark turquoise', font=('roboto', 12, 'bold'), bd=0)
    confirmEntry.grid(row=8, sticky='w', padx=15, )
    Frame(frame, width=200, height=2, bg='dark turquoise').grid(row=9, sticky='w', padx=20)

    submitButton = Button(frame, text='Submit', fg='white', font=('roboto', 10, 'bold'), bg='lime green',
                          activebackground='white', activeforeground='dark turquoise', width=29,
                          command=change_password)
    submitButton.grid(row=10, padx=10, pady=25)

    window.mainloop()


def signup_page():
    root.destroy()


def dashboard():
    root.destroy()


root = Tk()
root.geometry()
root.resizable(0, 0)
root.title("Login Page")


def signin():
    if user.get() == '' or passw.get() == '':
        messagebox.showerror("Error", "All Fields Are Required")
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='1')
            mycursor = con.cursor()
        except:
            mycursor.showerror('Error', 'Connection is not established')
            return
        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        mycursor.execute(query, (user.get(), passw.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid username and Password')
        else:
            messagebox.showerror('Success', 'Login Successful')


bgImage = ImageTk.PhotoImage(file='images.jpeg')
bgLabel = Label(root, image=bgImage)
bgLabel.grid(row=0, column=0)

frame = Frame(root, width=260, height=300, bg='white')
frame.place(x=350, y=30)

heading = Label(root, text="USER LOGIN", bg='white',
                font=('roboto', 20, 'bold'), fg='dark turquoise')
heading.place(x=400, y=30)


# Usernamefield


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, font=('roboto', 16, 'bold'),
             bd=0, fg='dark turquoise')
user.place(x=10, y=50, )
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=200, height=2, bg='dark turquoise').place(x=10, y=75)


#  password Field

def on_enter(e):
    passw.delete(0, 'end')


def on_leave(e):
    name = passw.get()
    if name == '':
        passw.insert(0, 'Password')


passw = Entry(frame, width=20, font=('roboto', 16, 'bold'),
              bd=0, fg='dark turquoise')
passw.place(x=10, y=90)
passw.insert(0, 'Password')
passw.bind('<FocusIn>', on_enter)
passw.bind('<FocusOut>', on_leave)

Frame(frame, width=200, height=2, bg='dark turquoise').place(x=10, y=115)

# forgot password

forgot = Button(frame, text='Forgot Password?', bd=0, bg='white',
                font=('roboto', 10, 'underline'), fg='dark turquoise',
                command=forgot_pass)

forgot.place(x=130, y=135)

# button

Button(frame, width=32, pady=7, text='Login', bg='lime green',
       fg='white', bd=0, command=signin).place(x=10, y=165)
label = Label(frame, width=20, text="Don't have an account ?",
              fg='dark turquoise', bg='white', font=('roboto', 10))
label.place(x=3, y=220)

sign_up = Button(frame, width=10, text='Create new', bg='white', bd=0,
                 font=('roboto', 10, 'bold underline'),
                 cursor='hand2', fg='Royalblue1', command=signup_page)

sign_up.place(x=160, y=220)

root.mainloop()
