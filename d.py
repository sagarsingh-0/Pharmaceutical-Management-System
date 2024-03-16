import os
import sqlite3
import time
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

from category import categoryClass
from employee import employeeClass
from product import productClass
from s import salesClass
from supplier import supplierClass


class PMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Dashboard")
        self.root.config(bg="white")

        # ===============title===========
        self.icon_title = Image.open("download.png")
        self.icon_title = self.icon_title.resize((90, 90), Image.ANTIALIAS)
        self.icon_title = ImageTk.PhotoImage(self.icon_title)

        title = Label(self.root, text="Pharmaceutical Management System", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20).place(x=0,
                                                                                                                 y=0,
                                                                                                                 relwidth=1,
                                                                                                                 height=70)
        # ==================button=============
        btn_logout = Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"),
                            bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)
        # ==================clock==========
        self.lbl_clock = Label(self.root,
                               text="Welcome to Pharmaceutical Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ===============left Menu===============
        self.MenuLogo = Image.open("WhatsApp Image 2023-05-23 at 17.31.08.jpg")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=540)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 18), bg="#009688").pack(side=TOP, fill=X)
        btn_employee = Button(LeftMenu, text="Employee", command=self.employee, font=("times new roman", 19, "bold"),
                              bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier", command=self.supplier, font=("times new roman", 19, "bold"),
                              bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="Category", command=self.category, font=("times new roman", 19, "bold"),
                              bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu, text="Product", command=self.product, font=("times new roman", 19, "bold"),
                             bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="Sale", command=self.s, font=("times new roman", 19, "bold"), bg="white",
                           bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="Exit", font=("times new roman", 19, "bold"), bg="white", bd=3,
                          cursor="hand2").pack(side=TOP, fill=X)

        # ==========Content========
        self.lbl_employee = Label(self.root, text="Total employee\n[ 0 ]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n[ 0 ]", bd=5, relief=RIDGE, bg="#ff5722", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Category\n[ 0 ]", bd=5, relief=RIDGE, bg="#009688", fg="white",
                                  font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Product\n[ 0 ]", bd=5, relief=RIDGE, bg="#607d8b", fg="white",
                                 font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE, bg="#ffc107", fg="white",
                               font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)

        # ===========Footer==========
        lbl_footer = Label(self.root,
                           text="PMS-Pharmaceutical Management System | Developed By : Sagar,Ayush,Chitta,Laxmipriya,Soumya,Suvashree\n\n",
                           font=("times new roman", 10), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)

        self.update_content()

        # ================

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def s(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = salesClass(self.new_win)

    def update_content(self):
        con = sqlite3.connect(database=r'pms.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            product = cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[ {str(len(product))} ]')

            cur.execute("select * from supplier")
            supplier = cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[ {str(len(supplier))} ]')

            cur.execute("select * from category")
            category = cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ {str(len(category))} ]')

            cur.execute("select * from employee")
            employee = cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[ {str(len(employee))} ]')
            bill = (len(os.listdir('bill')))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')

            time_ = time.strftime("%I:%M:%S")
            date_ = time.strftime("%d-%m-%Y")
            self.lbl_clock.config(
                text=f"Welcome to Pharmaceutical Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200, self.update_content)


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")


if __name__ == "__main__":
    root = Tk()
    obj = PMS(root)
    root.mainloop()