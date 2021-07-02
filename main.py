from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

def reg_win():
    rt.destroy()
    import register
def log_win():
    rt.destroy()
    import Login
rt=Tk()
rt.title("Home Page")
rt.geometry("1600x900+0+0")
imagebg=Image.open(r"images/bgmed.webp")
bg=ImageTk.PhotoImage(imagebg)
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)

upframe=Frame(rt,bd=5,relief=GROOVE,bg="white")
upframe.place(x=70,y=50,width=1220,height=150)

logo=Image.open(r"images/logo21.png")
logo11=ImageTk.PhotoImage(logo)
logolb=Label(upframe,image=logo11)
logolb.place(x=5,y=4)
title=Label(upframe,text="Welcome to Pharma Medicals",bd=6,relief=FLAT,font=("Sitka Text",35,"bold"),fg="#6B2737",bg="white")
title.place(x=150,y=10,width=750,height=70)
btnframe=Frame(upframe,bd=2,relief=FLAT,bg="white")
btnframe.place(x=920,y=20,width=290,height=80)
dashboard1=Button(btnframe,text="REGISTER",command=reg_win,bd=5,relief=RAISED,bg="#456990",fg="white",font=("System",15,"bold")).place(x=10,y=15,width=120,height=30)
addmedici=Button(btnframe,text="LOGIN",command=log_win,bd=5,relief=RAISED,bg="#456990",fg="white",font=("System",15,"bold")).place(x=140,y=15,width=120,height=30)
# logo2=Image.open(r"images/3.png")
# logo21=ImageTk.PhotoImage(logo2)
# logolb1=Label(upframe,image=logo21)
# logolb1.place(x=1050,y=3)


mainfrm=Frame(rt,bd=5,relief=GROOVE,bg="white")
mainfrm.place(x=70,y=170,width=1220,height=500)
logo2=Image.open(r"images/bgdown.jpg")
logo21=ImageTk.PhotoImage(logo2)
logolb1=Label(mainfrm,image=logo21)
logolb1.place(x=0,y=0)
rightfrm=Frame(mainfrm,bd=5,relief=RAISED,bg="white")
rightfrm.place(x=790,y=20,width=390,height=450)

imagebg1=Image.open(r"images/imgbg1.jpg")
bg1=ImageTk.PhotoImage(imagebg1)
bglb1=Label(rightfrm,image=bg1)
bglb1.place(x=0,y=0)
#114B5F
reg1=Label(rightfrm,text=r'"Bringing the medicine at your door.."',font=("Sitka Text",12,"bold italic"),fg="#F40000",bg="white")
reg1.place(x=0,y=415,width=380)

leftframe=Frame(mainfrm,bd=5,relief=GROOVE,bg="white")
leftframe.place(x=20,y=20,width=760,height=450)

lb=Label(leftframe,text="Everyone merits great wellbeing and at ‘PHARMA MEDICALS’ , \nyour wellbeing and prosperity is our need. For more than 100 years, \nwe have thought about the network with an extreme vision\n of making a more advantageous country, one part at any given moment.\n‘PHARMA MEDICALS’ is a common association where benefits\n made through activities are come back to individuals\n as advantages. We pride ourselves on giving amazing client\n administration and expert exhortation, \nalongside a wide scope of items and administrations.",font=("Monotype Corsiva",18,"bold"),bg="#F8F2DC",fg="#CD4631",justify=CENTER)
lb.place(x=15,y=10,width=710,height=400)

rt.mainloop()