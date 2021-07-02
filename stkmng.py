from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

def back():
    rt.destroy()
    import admin
def ls():
    db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
    mycursor=db.cursor()
    mycursor.execute("select * from med_info")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        tbdata.delete(*tbdata.get_children())
    for row in rows:
        if(int(row[5])<500):
            tbdata.insert('',END,values=[row[1],row[4],row[2],row[3],row[5]])
    db.commit()
    db.close()
    pass
def hs():
    db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
    mycursor=db.cursor()
    mycursor.execute("select * from med_info")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        tbdata.delete(*tbdata.get_children())
    for row in rows:
        if(int(row[5])>=500):
            tbdata.insert('',END,values=[row[1],row[4],row[2],row[3],row[5]])
    db.commit()
    db.close()
    pass
def deliverys():
    if mednm1.get()=="" or usernm1.get()=="" or delsts1.get()=="" or qty1.get()==""or medprice1.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        med_name=mednm1.get()
        med_stock=medprice1.get()
        # order_date_del=medst1.get()
        db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
        mycursor=db.cursor()
    try:
        sql="update med_info set med_stock=%s  where med_name=%s"
        val=(med_stock,med_name)
        mycursor.execute(sql,val)
        db.commit()
        messagebox.showinfo("information","stock updated successfully")
        clear()
        
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()
    showdata()

def clear():
    mednm1.delete(0,END)
    usernm1.delete(0, END)
    delsts1.delete(0, END)
    qty1.delete(0, END)
    medprice1.delete(0, END)
    mednm1.focus_set()
    pass
def getdata(event):
    currow=tbdata.focus()
    contents=tbdata.item(currow)
    row=contents['values']
    mednm1.delete(0,END)
    usernm1.delete(0, END)
    delsts1.delete(0, END)
    qty1.delete(0, END)
    medprice1.delete(0, END)
    mednm1.insert(0,row[0])
    usernm1.insert(0,row[1])
    delsts1.insert(0,row[2])
    qty1.insert(0,row[3])
    medprice1.insert(0,row[4])
def showdata():
    db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
    mycursor=db.cursor()
    mycursor.execute("select * from med_info")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        tbdata.delete(*tbdata.get_children())
    for row in rows:
        tbdata.insert('',END,values=[row[1],row[4],row[2],row[3],row[5]])
    db.commit()
    db.close()
    
rt=Tk()
rt.geometry("1600x900+0+0")
#====background=====
imagebg=Image.open(r"images/medico.jpg")
bg=ImageTk.PhotoImage(imagebg)
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)

rt.title("Manage Stock")
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
sidefrm.place(x=20,y=100,width=450,height=560)
stitle=Label(sidefrm,text="Stock Manager",font=("Sitka Text",20,"bold"),fg="white",bg="#457d69")
stitle.grid(row=0,columnspan=6,pady=10)
mednm=Label(sidefrm,text="Medicine Name",font=("Monotype Corsiva",16,"bold"),bg="#abdecc")
mednm.grid(row=2,column=0,padx=20,pady=10,sticky="w")
mednm1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
mednm1.grid(row=2,column=1,padx=20,pady=10,sticky="w")
usernm=Label(sidefrm,text="Medicine Price",font=("Monotype Corsiva",16,"bold"),bg="#abdecc")
usernm.grid(row=4,column=0,padx=20,pady=10,sticky="w")
usernm1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
usernm1.grid(row=4,column=1,padx=20,pady=10,sticky="w")
delsts=Label(sidefrm,text="Expiry Date",font=("Monotype Corsiva",16,"bold"),bg="#abdecc")
delsts.grid(row=6,column=0,padx=20,pady=10,sticky="w")
delsts1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
delsts1.grid(row=6,column=1,padx=20,pady=10,sticky="w")
qty=Label(sidefrm,text="Manufacture Date",font=("Monotype Corsiva",16,"bold"),bg="#abdecc")
qty.grid(row=8,column=0,padx=20,pady=10,sticky="w")
qty1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
qty1.grid(row=8,column=1,padx=20,pady=10,sticky="w")
medprice=Label(sidefrm,text="Quantity",font=("Monotype Corsiva",16,"bold"),bg="#abdecc")
medprice.grid(row=10,column=0,padx=20,pady=10,sticky="w")
medprice1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medprice1.grid(row=10,column=1,padx=20,pady=10,sticky="w")
# deladd=Label(sidefrm,text="Delivery Address",font=("Monotype Corsiva",16,"bold"),bg="#abdecc")
# deladd.grid(row=6,column=0,padx=20,pady=10,sticky="w")
# deladd1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
# deladd1.grid(row=6,column=1,padx=20,pady=10,sticky="w")

#Buttons
btnframe=Frame(sidefrm,bd=7,relief=RIDGE,bg="#231B1B")
btnframe.place(x=25,y=380,width=350,height=70)

delivery=Button(btnframe,text="UPDATE STOCK",command=deliverys,bd=5,relief=RAISED,width=16,font=("System",10,"bold")).grid(row=4,column=0,padx=10,pady=10)
# deletebtn=Button(btnframe,text="DELETE",command=delete,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=4,column=1,padx=10,pady=10)
clearbtn=Button(btnframe,text="CLEAR",command=clear,bd=5,relief=RAISED,width=15,font=("System",10,"bold")).grid(row=4,column=2,padx=10,pady=10)
# backbtn=Button(btnframe,text="Back",command=back,bd=5,relief=RAISED,width=7,font=("System",10,"bold")).grid(row=4,column=3,padx=10,pady=10)




#rightframe
mainfrm=Frame(rt,bd=5,relief=GROOVE,bg="#abdecc")
mainfrm.place(x=490,y=100,width=840,height=560)
maintitle=Label(mainfrm,text="Stock Details",font=("Sitka Text",25,"bold"),fg="white",bg="#457d69")
maintitle.place(x=190,y=10,width=400,height=40)

searchfrm=Frame(mainfrm,bd=5,relief=FLAT,bg="white")
searchfrm.place(x=15,y=70,width=800,height=450)
# searchlb=Label(searchfrm,text="Search By",font=("Monotype Corsiva",18,"bold"),bg="white")
# searchlb.grid(row=0,column=0,padx=10,pady=10,sticky="w")
# searchbar=ttk.Combobox(searchfrm,width=10,font=("Times New Roman",13,"bold"),state="readonly")
# # searchbar['values']=("med_id","med_name")
# searchbar['values']=("med_name","user_fname")
# searchbar.grid(row=0,column=1,padx=20,pady=10)
# lsearch=Entry(searchfrm,font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE)
# lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")
searchbt=Button(searchfrm,text="LOW STOCK",command=ls,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=3,padx=10,pady=10)
searchbt=Button(searchfrm,text="HIGH STOCK",command=hs,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=4,padx=10,pady=10)
searchbt=Button(searchfrm,text="SHOW ALL",command=showdata,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=5,padx=10,pady=10)

tbframe=Frame(searchfrm,bd=4,relief=RIDGE,bg="#C1CAD6")
tbframe.place(x=20,y=60,width=720,height=360)
scrollx=Scrollbar(tbframe,orient=HORIZONTAL)
scrolly=Scrollbar(tbframe,orient=VERTICAL)
tbdata=ttk.Treeview(tbframe,columns=("mednm","usernm","delsts","qty","medprice"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=tbdata.xview)
scrolly.config(command=tbdata.yview)
tbdata.heading("mednm",text="Medicine Name")
tbdata.heading("usernm",text="Medicine Price")
tbdata.heading("delsts",text="Expiry Date")
tbdata.heading("qty",text="Manufacture Date")
tbdata.heading("medprice",text="Quantity")
# tbdata.heading("deladd",text="Delivery Address")
tbdata['show']="headings"
tbdata.column("mednm",width=100)
tbdata.column("usernm",width=100)
tbdata.column("delsts",width=100)
tbdata.column("qty",width=100)
tbdata.column("medprice",width=100)
# tbdata.column("deladd",width=100)
tbdata.pack(fill=BOTH,expand=1)
tbdata.bind("<ButtonRelease-1>",getdata)
showdata()
rt.mainloop()