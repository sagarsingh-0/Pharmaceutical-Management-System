import subprocess
from tkinter import *

from PIL import ImageTk


def sign():
    win.destroy()
    subprocess.run(["python", "login.py"])  # Run the login.py script using subprocess


win = Tk()
win.geometry('360x360')
win.title("Splashscreen")

bgImage = ImageTk.PhotoImage(file='IMG_20230319_222623.jpg')

bgLabel = Label(win, image=bgImage)
bgLabel.place(x=0, y=0)

l1 = Label(win, text="PHARMACEUTICAL MANAGEMENT SYSTEM", bg='white',
           font=('roboto', 10, 'bold'), fg='dark turquoise')
l1.place(x=35, y=70)

win.after(3000, sign)

win.mainloop()
