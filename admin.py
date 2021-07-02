from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

def dashboard(): 
    pass
def addmed():
    rt.destroy()
    import addmed
def logout():
    rt.destroy()
    import Login
def delivery():
    rt.destroy()
    import delievery
def medstock():
    rt.destroy()
    import stkmng
def userhis():
    rt.destroy()
    import userhistory
    pass




rt=Tk()
rt.title("Admin Page")
rt.geometry("1600x900+0+0")
imagebg=Image.open(r"images/medico.jpg")
bg=ImageTk.PhotoImage(imagebg)
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)

title=Label(rt,text="Admin Panel",bd=6,relief=GROOVE,font=("Sitka Text",35,"bold"),fg="#4E148C",bg="white")
title.place(x=220,y=80,width=900,height=70)
# img2=Image.open(r"images\userpic.png")
# img2=img2.resize((25,25),Image.ANTIALIAS)

topframe=Frame(rt,bd=5,relief=GROOVE,bg="white")
topframe.place(x=220,y=150,width=900,height=500)

btnframe=Frame(topframe,bd=5,relief=RIDGE,bg="#d3d3d3")
btnframe.place(x=10,y=10,width=180,height=450)
dashboard1=Button(btnframe,text="DASHBOARD",command=dashboard,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=50,width=170,height=70)
addmedici=Button(btnframe,text="ADD MEDICINE",command=addmed,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=120,width=170,height=70)
userHis=Button(btnframe,text="USER HISTORY",command=userhis,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=190,width=170,height=70)
stock=Button(btnframe,text="MEDICINE STOCK",command=medstock,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=260,width=170,height=70)
delivery1=Button(btnframe,text="DELIVERY STATUS",command=delivery,bd=5,relief=RAISED,font=("System",10,"bold")).place(x=0,y=330,width=170,height=70)

reg=Label(topframe,text="Welcome Admin!!",font=("Monotype Corsiva",35,"bold"),fg="darkgreen",bg="white")
reg.place(x=200,y=30,width=370)
logout11=Button(topframe,text="LOGOUT",command=logout,bd=5,relief=RAISED,bg="#456990",fg="white",font=("System",15,"bold")).place(x=650,y=50,width=120,height=30)
# adminimg=Image.open(r"images/doc.jpg")
# adminpl=ImageTk.PhotoImage(adminimg)
# userpl=Label(topframe,image=adminpl,bd=2,relief=FLAT)
# userpl.place(x=280,y=30)


img1=Image.open(r"images/product1.jpg")
img1lb=ImageTk.PhotoImage(img1)
bglb1=Label(topframe,image=img1lb)
bglb1.place(x=250,y=120)
reg1=Label(topframe,text="Product Manager",font=("Monotype Corsiva",18,"bold"),fg="darkgreen",bg="white")
reg1.place(x=250,y=260,width=200)

img2=Image.open(r"images/users21.png")
img2lb=ImageTk.PhotoImage(img2)
bglb2=Label(topframe,image=img2lb)
bglb2.place(x=550,y=120)
reg1=Label(topframe,text="Users History",font=("Monotype Corsiva",18,"bold"),fg="darkgreen",bg="white")
reg1.place(x=550,y=260,width=200)

img3=Image.open(r"images/medbg1.jpg")
img3lb=ImageTk.PhotoImage(img3)
bglb3=Label(topframe,image=img3lb)
bglb3.place(x=250,y=320)
reg2=Label(topframe,text="Medicine Stock",font=("Monotype Corsiva",18,"bold"),fg="darkgreen",bg="white")
reg2.place(x=250,y=430,width=200)


img4=Image.open(r"images/cartpro.png")
img4lb=ImageTk.PhotoImage(img4)
bglb4=Label(topframe,image=img4lb)
bglb4.place(x=550,y=320)
reg3=Label(topframe,text="Public Products",font=("Monotype Corsiva",18,"bold"),fg="darkgreen",bg="white")
reg3.place(x=550,y=430,width=200)

rt.mainloop()