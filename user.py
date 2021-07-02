from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox 
from PIL import Image,ImageTk
# from Login import user_name
# import mysql.connector
def dashboard():
    pass
def viewmed():
    rt.destroy()
    import viewmed
def medorder():
    rt.destroy()
    import medreq
def changepass():
    import forgetpass
def logout():
    rt.destroy()
    import Login
rt=Tk()
# print(user_name)
rt.title("User Page")
rt.geometry("1600x900+0+0")
imagebg=Image.open(r"images/medico.jpg")
bg=ImageTk.PhotoImage(imagebg)
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)

title=Label(rt,text="User Panel",bd=6,relief=GROOVE,font=("Sitka Text",35,"bold"),fg="#4E148C",bg="white")
title.place(x=220,y=80,width=900,height=70)
# img2=Image.open(r"images\userpic.png")
# img2=img2.resize((25,25),Image.ANTIALIAS)

topframe=Frame(rt,bd=5,relief=GROOVE,bg="white")
topframe.place(x=220,y=150,width=900,height=500)

btnframe=Frame(topframe,bd=5,relief=RIDGE,bg="#d3d3d3")
btnframe.place(x=10,y=10,width=180,height=450)
dashboard=Button(btnframe,text="DASHBOARD",command=dashboard,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=50,width=170,height=70)
addmedici=Button(btnframe,text="VIEW MEDICINE",command=viewmed,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=120,width=170,height=70)
userHis=Button(btnframe,text="ORDER MEDICINE",command=medorder,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=190,width=170,height=70)
stock=Button(btnframe,text="CHANGE PASSWORD",command=changepass,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=260,width=170,height=70)
logout=Button(btnframe,text="LOGOUT",command=logout,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=330,width=170,height=70)

reg=Label(topframe,text=f"Welcome user !!",font=("Monotype Corsiva",35,"bold"),fg="darkgreen",bg="white")
reg.place(x=200,y=15,width=370)
# adminimg=Image.open(r"images/doc.jpg")
# adminpl=ImageTk.PhotoImage(adminimg)
# userpl=Label(topframe,image=adminpl,bd=2,relief=FLAT)
# userpl.place(x=280,y=30)


img1=Image.open(r"images/pro1.jpg")
img1lb=ImageTk.PhotoImage(img1)
bglb1=Label(topframe,image=img1lb)
bglb1.place(x=250,y=100)
reg1=Label(topframe,text="View Medicine",font=("Monotype Corsiva",18,"bold"),fg="darkgreen",bg="white")
reg1.place(x=250,y=240,width=200)

img2=Image.open(r"images/customer.jpg")
img2lb=ImageTk.PhotoImage(img2)
bglb2=Label(topframe,image=img2lb)
bglb2.place(x=550,y=100)
reg1=Label(topframe,text="Your Order History",font=("Monotype Corsiva",18,"bold"),fg="darkgreen",bg="white")
reg1.place(x=550,y=240,width=200)

img3=Image.open(r"images/medi.jpg")
img3lb=ImageTk.PhotoImage(img3)
bglb3=Label(topframe,image=img3lb)
bglb3.place(x=250,y=300)
reg2=Label(topframe,text="View Cart",font=("Monotype Corsiva",18,"bold"),fg="darkgreen",bg="white")
reg2.place(x=250,y=440,width=200)


img4=Image.open(r"images/doctor1.jpg")
img4lb=ImageTk.PhotoImage(img4)
bglb4=Label(topframe,image=img4lb)
bglb4.place(x=550,y=300)
reg3=Label(topframe,text="View Profile",font=("Monotype Corsiva",18,"bold"),fg="darkgreen",bg="white")
reg3.place(x=550,y=440,width=200)

rt.mainloop()