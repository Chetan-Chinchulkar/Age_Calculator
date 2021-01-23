#Importing libraries from python packages

from tkinter import *
from datetime import date
import time

#Command for Calculate Button

def Proceed():
    D=D_en.get()
    M=M_en.get()
    Y=Y_en.get()

    D=int(D)
    M=int(M)
    Y=int(Y)

    err=Validate(D,M,Y)

    if err=='y':
        Err_lb.configure(text="Enter Correct Year")
        Out_lb.configure(text='')
        DOB_lb.configure(text='')
        Y_en.delete(0,END)
    elif err=='m':
        Err_lb.configure(text="Enter Correct Month")
        Out_lb.configure(text='')
        DOB_lb.configure(text='')
        M_en.delete(0,END)
    elif err=='d':
        Err_lb.configure(text="Enter Correct Date")
        Out_lb.configure(text='')
        DOB_lb.configure(text='')
        D_en.delete(0,END)
    elif err=='a':
        Err_lb.configure(text="Enter Correct Date")
        Out_lb.configure(text='')
        DOB_lb.configure(text='')
        D_en.delete(0,END)
        M_en.delete(0,END)
        Y_en.delete(0,END)
    else:
        Err_lb.configure(text='')
        Calc(D,M,Y)
        D_en.delete(0,END)
        M_en.delete(0,END)
        Y_en.delete(0,END)


#Validate the entered date,month and year

def Validate(D,M,Y):
    Dt=date.today()
    Dt=str(Dt)

    Cr_dt_lb.configure(text="Current Date :{0}".format(Dt))

    Cr_Yr=Dt[:4]
    Cr_Yr=int(Cr_Yr)

    if Y>Cr_Yr or Y<1947:
        return 'y'
    elif D>31 and M>12 and Y>Cr_Yr:
        return 'a'
    if M>12:
        return 'm'
    elif D>31:
        return 'd'
    elif (M in M_31) and D>31:
        return 'd'
    elif (M in M_30) and D>30:
        return 'd'
    elif (M in M_28) and Y%4==0 and D>29:
        return 'd'
    elif (M in M_28) and Y%4!=0 and D>28:
        return 'd'
    else:
        return 'n'

#Calculating the age of the user

def Calc(D,M,Y):
    Dt=date.today()
    Dt=str(Dt)

    Cr_Yr=Dt[:4]

    Cr_Mn=Dt[5:7]
    Cr_Dt=Dt[8:]
    Cr_Dt=int(Cr_Dt)
    Cr_Mn=int(Cr_Mn)
    Cr_Yr=int(Cr_Yr)

    YY=Cr_Yr-Y
    MM=Cr_Mn-M
    DD=Cr_Dt-D

    if D>Cr_Dt:
        M=M-1
        MM=MM-1
        if M in M_31:
            DD=31+DD
        elif M in M_30:
            DD=30+DD
        elif M in M_28 and Y%4==0:
            DD=28+DD
        else:
            DD=29+DD
        M=M+1
    if M>Cr_Mn:
        YY=YY-1
        MM=12+MM

    DOB=str(D)+'/'+str(M)+'/'+str(Y)

    DOB_lb.configure(text="Your DOB :{0}".format(DOB))

    Cr_Age=str(str(YY)+' years '+str(MM)+' months '+str(DD)+' days old ')

    Out_lb.configure(text="Your Current Age is \n{0}".format(Cr_Age))

#lists for months

M_31=[1,3,5,7,8,10,12]
M_30=[4,6,11]
M_28=[2]

#Creating GUIs using Tkinter functions

win=Tk()
win.title('Age Calculator')
win.configure(bg='Light Green')
win.geometry('1200x550')

D_lb=Label(text='Enter Date of Birth',font=('Algerian',20),bg='Light Green',fg='Grey')
D_lb.grid(row=1,column=0)
M_lb=Label(text='Enter Month of Birth',font=('Algerian',20),bg='Light Green',fg='Grey')
M_lb.grid(row=2,column=0)
Y_lb=Label(text='Enter Year of Birth',font=('Algerian',20),bg='Light Green',fg='Grey')
Y_lb.grid(row=3,column=0)

D_en=Entry(font=('Algerian',20),bg='Light Grey',fg='Yellow',width=10)
D_en.grid(row=1,column=1)
M_en=Entry(font=('Algerian',20),bg='Light Grey',fg='Yellow',width=10)
M_en.grid(row=2,column=1)
Y_en=Entry(font=('Algerian',20),bg='Light Grey',fg='Yellow',width=10)
Y_en.grid(row=3,column=1)

Cal_But=Button(text='Calculate Age',font=('Algerian',20),bg='Magenta',command=Proceed)
Cal_But.grid(row=2,column=2)

Ext_But=Button(text='Exit',font=('Algerian',20),bg='Magenta',command=exit)
Ext_But.grid(row=2,column=3)

Err_lb=Label(font=('Algerian',20),bg='Light Green')
Err_lb.grid(row=5,column=0)

Cr_dt_lb=Label(font=('',20),bg='Light Green')
Cr_dt_lb.grid(row=0,column=1)

DOB_lb=Label(font=('',20),bg='Light Green')
DOB_lb.grid(row=5,column=1)

Out_lb=Label(font=('Algerian',20),bg='Light Green')
Out_lb.grid(row=6,column=1)

Nm_lb=Label(text="App made by \n\tCHETAN CHINCHULKAR",font=('',20),bg='Light Green',fg='Red')
Nm_lb.grid(row=8,column=0)

win.mainloop()
