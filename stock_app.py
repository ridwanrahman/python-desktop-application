from tkinter import *
from tkinter import Tk, StringVar, ttk
import random
import datetime

root = Tk()
root.geometry("1350x750+0+0")
root.title("stock control system")

TopFrame = Frame(root, width=1350, height=100, bd=14, relief='raise')
TopFrame.pack(side=TOP)

BottomFrame = Frame(root, width=1350, height=200, bd=14, relief='raise')
BottomFrame.pack(side=BOTTOM)

LeftMidFrame = Frame(BottomFrame, width=600, height=1000, bd=14, relief='raise')
LeftMidFrame.pack(side=LEFT)
RightMidFrame = Frame(BottomFrame, width=750, height=1000, bd=14, relief='raise')
RightMidFrame.pack(side=RIGHT)

lblTitle = Label(TopFrame, font=('arial', 40, 'bold'), text="STOCK control system", bd=10, width=41, justify='center')
lblTitle.grid(row=0, column=0)

# ============================ Variables =====================================================
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

var1.set("0")
# ============================ Product Detail =====================================================

lblProductID = Label(LeftMidFrame, font=('arial', 18, 'bold'), text="Product id", bd=10, width=20, anchor='w')
lblProductID.grid(row=0, column=0)
cmbProductID = ttk.Combobox(LeftMidFrame, textvariable=var1, state='readonly', font=('arial', 18, 'bold'), width=18)
cmbProductID['value'] = ('', 'PID002', 'PID003', 'PID004', 'PID005', 'PID006')
cmbProductID.current(0)
cmbProductID.grid(row=0, column=1)

lblProductName1 = Label(LeftMidFrame, font=('arial', 18, 'bold'), text="Product Name", bd=10, width=20, anchor='w')
lblProductName1.grid(row=1, column=0)
lblProductName2 = Label(LeftMidFrame, font=('arial', 18, 'bold'), textvariable=var1, bd=10, width=18, relief='sunken')
lblProductName2.grid(row=1, column=1)

lblDescription1 = Label(LeftMidFrame, font=('arial', 18, 'bold'), text="Description 1", bd=10, width=20, anchor='w')
lblDescription1.grid(row=1, column=0)
lblDescription2 = Label(LeftMidFrame, font=('arial', 18, 'bold'), text="Description 2", bd=10, width=20, anchor='w')
lblDescription2.grid(row=1, column=0)



root.mainloop()
