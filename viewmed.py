from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

def search():
    ser1=searchbar.get()
    lsearch1=lsearch.get()
    if(lsearch1=="" or ser1==""):
        messagebox.showerror("Error","Empty Field")
    else:
        db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
        mycursor=db.cursor()
        mycursor.execute("select * from med_info where "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")
        rows=mycursor.fetchall()
        if len(rows)!=0:
            tbdata.delete(*tbdata.get_children())
        for row in rows:
            tbdata.insert('',END,values=[row[1:2],row[3:4],row[2:3],row[4:5],row[6]])
        db.commit()
        db.close()
        lsearch.delete(0,END)
        searchbar.delete(0,END)

def back():
    rt.destroy()
    import user
def medre():
    rt.destroy()
    import medreq
def showdata():
    
    db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
    mycursor=db.cursor()
    mycursor.execute("select * from med_info")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        tbdata.delete(*tbdata.get_children())
    for row in rows:
        tbdata.insert('',END,values=[row[1],row[3],row[2],row[4],row[6]])
    db.commit()
    db.close()


rt=Tk()
rt.geometry("1600x900+0+0")
#====background=====
imagebg=Image.open(r"images/medico.jpg")
bg=ImageTk.PhotoImage(imagebg)
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)

rt.title("View Medicine")
title=Label(rt,text="Pharma Medicals",bd=8,relief=SUNKEN,font=("Sitka Text",35,"bold"),fg="#66101F",bg="white")
title.pack(side=TOP,fill=X)
backbtn=Button(rt,text="BACK",command=back,bd=5,relief=RAISED,width=7,font=("System",10,"bold"),bg="#755B69",fg="white")
backbtn.place(x=30,y=20,width=90,height=40)
logo=Image.open(r"images/logo21.png")
logo11=ImageTk.PhotoImage(logo)
logolb=Label(image=logo11)
logolb.place(x=360,y=20,width=100,height=54)
#C1CAD6
sidefrm=Frame(rt,bd=5,relief=GROOVE,bg="#abdecc")
sidefrm.place(x=54,y=100,width=404,height=170)

lb=Label(sidefrm,text='"Yesterday is not ours\n to recover, \nbut tomorrow is ours \nto win or lose."',font=("Sitka Text",15,"bold italic"),bg="#abdecc",fg="#66101F",justify=CENTER)
lb.place(x=44,y=0,width=300,height=170)

img1=Image.open(r"images\pharmacy-hero1.png")
img1lb=ImageTk.PhotoImage(img1)
bglb1=Label(image=img1lb)
bglb1.place(x=54,y=264)




#rightframe
mainfrm=Frame(rt,bd=5,relief=GROOVE,bg="#abdecc")
mainfrm.place(x=490,y=100,width=840,height=560)
maintitle=Label(mainfrm,text="View Medicine Detalis",font=("Sitka Text",20,"bold"),fg="white",bg="#457d69")
maintitle.place(x=190,y=10,width=400,height=40)

searchfrm=Frame(mainfrm,bd=5,relief=FLAT,bg="white")
searchfrm.place(x=15,y=70,width=800,height=450)
searchlb=Label(searchfrm,text="Search By",font=("Monotype Corsiva",18,"bold"),bg="white")
searchlb.grid(row=0,column=0,padx=10,pady=10,sticky="w")
searchbar=ttk.Combobox(searchfrm,width=10,font=("Times New Roman",13,"bold"),state="readonly")
# searchbar['values']=("med_id","med_name")
searchbar['values']=("med_name","med_id")
searchbar.grid(row=0,column=1,padx=20,pady=10)
lsearch=Entry(searchfrm,font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE)
lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")

searchbt=Button(searchfrm,text="SEARCH",command=search,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=4,padx=10,pady=10)
searchbt=Button(searchfrm,text="ORDER NOW",command=medre,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=5,padx=10,pady=10)

tbframe=Frame(searchfrm,bd=4,relief=RIDGE,bg="#C1CAD6")
tbframe.place(x=20,y=60,width=720,height=360)
scrollx=Scrollbar(tbframe,orient=HORIZONTAL)
scrolly=Scrollbar(tbframe,orient=VERTICAL)
tbdata=ttk.Treeview(tbframe,columns=("mednm","medman","medexp","medprice","desc"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=tbdata.xview)
scrolly.config(command=tbdata.yview)
tbdata.heading("mednm",text="Medicine Name")
tbdata.heading("medman",text="Manufacture Date")
tbdata.heading("medexp",text="Expiry Date")
tbdata.heading("medprice",text="Medicine Price")
tbdata.heading("desc",text="Description")
tbdata['show']="headings"
tbdata.column("mednm",width=100)
tbdata.column("medman",width=100)
tbdata.column("medexp",width=100)
tbdata.column("medprice",width=100)
tbdata.column("desc",width=100)
tbdata.pack(fill=BOTH,expand=1)
tbdata.bind("<ButtonRelease-1>")
showdata()
rt.mainloop()