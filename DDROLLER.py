from tkinter import *
import random
from tkinter import messagebox
import time


root=Tk()
root.configure(background='#0B0B0B')
root.title("Dark")

#Warking
def warning():
    messagebox.showinfo('Warning', "If you feel that the roller isn't updating use the 'Clear All' button.")

#Dice
def clear():
    root.after(15)
    text_input4.set('')
    text_input6.set('')
    text_input10.set('')
    text_input10x2.set('')
    text_input12.set('')
    text_input20.set('')
def NumbergenD4():
    d4=random.randint(1,4)
    text_input4.set(d4)
def NumbergenD6():
    d6=random.randint(1,6)
    text_input6.set(d6)
def NumbergenD10():
    d10=random.randint(0,9)
    d10=d10*10
    text_input10.set(d10)
    if d10==0:
        text_input10.set('00')
def NumbergenD10x2():
    d10x2=random.randint(0,9)
    text_input10x2.set(d10x2)
def NumbergenD12():
    d12=random.randint(1,12)
    text_input12.set(d12)
def NumbergenD20():
    d20=random.randint(1,20)
    text_input20.set(d20)

text_input4=StringVar()
text_input6=StringVar()
text_input10=StringVar()
text_input10x2=StringVar()
text_input12=StringVar()
text_input20=StringVar()

#Entries
TD1= Entry (root, font = 'arial 35 bold',textvariable=text_input4, width=4, bd=10, bg ='#282828',fg='#ff0000', justify = 'right').grid(row=0, column=1)
TD2= Entry (root, font = 'arial 35 bold',textvariable=text_input6,width=4, bd=10, bg = '#282828',fg='#ff0000', justify = 'right').grid(row=1, column=1)
TD3= Entry (root, font = 'arial 35 bold',textvariable=text_input10, width=4, bd=10, bg = '#282828',fg='#ff0000', justify = 'right').grid(row=2, column=1)
TD4= Entry (root, font = 'arial 35 bold',textvariable=text_input10x2, width=4, bd=10, bg = '#282828',fg='#ff0000', justify = 'right').grid(row=3, column=1)
TD5= Entry (root, font = 'arial 35 bold',textvariable=text_input12, width=4, bd=10, bg = '#282828',fg='#ff0000', justify = 'right').grid(row=4, column=1)
TD6= Entry (root, font = 'arial 35 bold',textvariable=text_input20, width=4, bd=10, bg = '#282828',fg='#ff0000', justify = 'right').grid(row=5, column=1)

#Buttons
btfD4 = Button(root,text= "D4",font = 'arial 10 bold', fg = 'Crimson', bg='#3E3E3E', width=12,height=3,command=NumbergenD4).grid(row=0,column=0)
btfD6=Button(root,text= "D6",font = 'arial 10 bold', fg = 'Crimson', bg='#3E3E3E', width=12,height=3,command=NumbergenD6).grid(row=1,column=0)
btfD10=Button(root,text= "D10 (Tens)",font = 'arial 10 bold', fg = 'Crimson', bg='#3E3E3E', width=12,height=3, command=NumbergenD10).grid(row=2,column=0)
btfD10x2=Button(root,text= "D10 (Ones)",font = 'arial 10 bold', fg = 'Crimson', bg='#3E3E3E', width=12,height=3,command=NumbergenD10x2).grid(row=3,column=0)
btfD12=Button(root,text= "D12",font = 'arial 10 bold', fg = 'Crimson', bg='#3E3E3E', width=12,height=3,command=NumbergenD12).grid(row=4,column=0)
btfD20=Button(root,text= "D20",font = 'arial 10 bold', fg = 'Crimson', bg='#3E3E3E', width=12,height=3,command=NumbergenD20).grid(row=5,column=0)
Clearbtn=Button(root,text="Clear All", font='arial 10 bold', fg='Crimson', bg='#3E3E3E', width=14,height=1, command=clear).grid(row=6,column=1)
Warning=Button(root,text="Keep in mind", font='arial 10 bold', fg='Crimson', bg='#3E3E3E', width=14,height=1, command=warning).grid(row=6,column=0)

root.mainloop()
