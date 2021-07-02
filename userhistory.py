from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
def back():
    rt.destroy()
    import admin

def approve():
    if mednm1.get()=="" or medadd1.get()=="" or user_name1.get()=="" or med_track1.get()==""or medprice1.get()=="" or medst1.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        order_id=med_track1.get()
        order_date_del=medst1.get()
        med_quan=user_name1.get()
        db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
        mycursor=db.cursor()
    try:
        sql="update med_order_req set order_status=%s, order_date_del=%s  where order_id=%s"
        val=("approved",order_date_del,int(order_id))
        mycursor.execute(sql,val)
        db.commit()
        messagebox.showinfo("information","Order Confirmed successfully")
        showdata()
        mycursor.execute("select * from med_order_req where order_id=%s",(int(order_id),))
        row=mycursor.fetchone()
        med_id=row[2]
        mycursor.execute("select * from med_info where med_id=%s",(int(med_id),))
        row=mycursor.fetchone()
        med_stk=int(row[5])-int(med_quan)
        mycursor.execute("update med_info set med_stock=%s where med_id=%s",(str(med_stk),med_id))
        db.commit()
        db.close()
        clearall()
        
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()
    pass
def reject():
    if mednm1.get()=="" or medadd1.get()=="" or user_name1.get()=="" or med_track1.get()==""or medprice1.get()=="" :
        messagebox.showerror("Error","All fields are required")
    else:
        order_id=med_track1.get()
        # order_date_del=medst1.get()
        db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
        mycursor=db.cursor()
    try:
        sql="update med_order_req set order_status=%s, order_date_del=%s  where order_id=%s"
        val=("rejected","-",order_id)
        mycursor.execute(sql,val)
        db.commit()
        messagebox.showinfo("information","Order rejected successfully")
        clearall()
        
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()
    showdata()
    pass
# def price():
#     med_name=mednm1.get()
#     db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
#     mycursor=db.cursor()
#     sql="delete from med_info where med_name=%s"
#     val=(med_name,)
#     mycursor.execute(sql,val)
#     db.commit()
#     db.close()
#     messagebox.showinfo("information","deleted successfully")
#     clearall()
#     showdata()
        

def clearall():
    mednm1.delete(0,END)
    medadd1.delete(0, END)
    user_name1.delete(0, END)
    med_track1.delete(0, END)
    medprice1.delete(0, END)
    medst1.delete(0, END)
    mednm1.focus_set()

def showdata():
    # med_name=mednm1.get()
    # med_exp=medadd1.get()
    # med_mfd=user_name1.get()
    # med_desc=med_track1.get()
    # med_price=medprice1.get()
    # med_stock=medst1.get()
    db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
    mycursor=db.cursor()
    mycursor.execute("select * from med_order_req")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        tbdata.delete(*tbdata.get_children())
    for row in rows:
        med_id=row[2]
        user_id=row[1]
        mycursor.execute("select * from med_info where med_id=%s",(med_id,))
        info=mycursor.fetchone()
       
        med_nm=info[1]
        mycursor.execute("select * from user_info where user_id=%s",(user_id,))
        info1=mycursor.fetchone()
        user_nm=info1[2]
        tbdata.insert('',END,values=[med_nm,row[3],user_nm,row[5],row[4],row[8],row[9],row[0]])
    db.commit()
    db.close()
def getdata(event):
    currow=tbdata.focus()
    contents=tbdata.item(currow)
    row=contents['values']
    mednm1.delete(0,END)
    medadd1.delete(0, END)
    user_name1.delete(0, END)
    med_track1.delete(0, END)
    medprice1.delete(0, END)
    medst1.delete(0, END)
    mednm1.insert(0,row[0])
    medadd1.insert(0,row[1])
    user_name1.insert(0,row[4])
    med_track1.insert(0,row[7])
    medprice1.insert(0,row[3])
    # medst1.insert(0,row[6])
    

rt=Tk()
rt.geometry("1600x900+0+0")
rt.title("Add Medicine")
title=Label(rt,text="Pharma Medicals",bd=8,relief=SUNKEN,font=("Sitka Text",35,"bold"),fg="#66101F",bg="#C1CAD6")
title.pack(side=TOP,fill=X)
backbtn=Button(rt,text="BACK",command=back,bd=5,relief=RAISED,width=7,font=("System",10,"bold"),bg="#755B69",fg="white")
backbtn.place(x=30,y=20,width=90,height=40)
#C1CAD6
sidefrm=Frame(rt,bd=5,relief=GROOVE,bg="#C1CAD6")
sidefrm.place(x=20,y=100,width=450,height=560)
stitle=Label(sidefrm,text="EDIT REQUEST",font=("Sitka Text",20,"bold"),fg="#0F5257",bg="#C1CAD6")
stitle.grid(row=0,columnspan=2,pady=10)
mednm=Label(sidefrm,text="Medicine Name",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
mednm.grid(row=1,column=0,padx=20,pady=10,sticky="w")

mednm1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
mednm1.grid(row=1,column=1,padx=20,pady=10,sticky="w")

medadd=Label(sidefrm,text="ADDRESS",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
medadd.grid(row=2,column=0,padx=20,pady=10,sticky="w")

medadd1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medadd1.grid(row=2,column=1,padx=20,pady=10,sticky="w")

user_name=Label(sidefrm,text="QUANTITY",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
user_name.grid(row=3,column=0,padx=20,pady=10,sticky="w")

user_name1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
user_name1.grid(row=3,column=1,padx=20,pady=10,sticky="w")

med_track=Label(sidefrm,text="ORDER ID",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
med_track.grid(row=4,column=0,padx=20,pady=10,sticky="w")

med_track1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
med_track1.grid(row=4,column=1,padx=20,pady=10,sticky="w")

medprice=Label(sidefrm,text="Medicine Price",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
medprice.grid(row=5,column=0,padx=20,pady=10,sticky="w")

medprice1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medprice1.grid(row=5,column=1,padx=20,pady=10,sticky="w")

medstock=Label(sidefrm,text="DELIEVERY DATE",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
medstock.grid(row=6,column=0,padx=20,pady=10,sticky="w")

medst1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medst1.grid(row=6,column=1,padx=20,pady=10,sticky="w")

#Buttons
btnframe=Frame(sidefrm,bd=7,relief=RIDGE,bg="darkgray")
btnframe.place(x=15,y=410,width=390,height=70)

addbtn=Button(btnframe,text="APPROVE",command=approve,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=4,column=0,padx=10,pady=10)
addbtn=Button(btnframe,text="REJECT",command=reject,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=4,column=1,padx=10,pady=10)
addbtn=Button(btnframe,text="CLEAR",command=clearall,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=4,column=3,padx=10,pady=10)


#rightframe
mainfrm=Frame(rt,bd=5,relief=GROOVE,bg="#C1CAD6")
mainfrm.place(x=490,y=100,width=840,height=560)
maintitle=Label(mainfrm,text="USER REQUEST",font=("Sitka Text",20,"bold"),fg="#0F5257",bg="#C1CAD6")
maintitle.place(x=190,y=10,width=400,height=40)

searchfrm=Frame(mainfrm,bd=5,relief=FLAT,bg="white")
searchfrm.place(x=15,y=70,width=800,height=450)


tbframe=Frame(searchfrm,bd=4,relief=RIDGE,bg="#C1CAD6")
tbframe.place(x=30,y=40,width=720,height=360)
scrollx=Scrollbar(tbframe,orient=HORIZONTAL)
scrolly=Scrollbar(tbframe,orient=VERTICAL)
tbdata=ttk.Treeview(tbframe,columns=("mednm","medman","medexp","medprice","stock","desc","date","orderid"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=tbdata.xview)
scrolly.config(command=tbdata.yview)
tbdata.heading("mednm",text="Medicine Name")
tbdata.heading("medman",text="ADDRESS")
tbdata.heading("medexp",text="USER NAME")
tbdata.heading("medprice",text="Medicine Price")
tbdata.heading("stock",text="Quantity")
tbdata.heading("desc",text="TRACK ORDER")
tbdata.heading("date",text="DELIEVERY DATE")
tbdata.heading("orderid",text="ORDER ID")
tbdata['show']="headings"
tbdata.column("mednm",width=100)
tbdata.column("medman",width=80)
tbdata.column("medexp",width=75)
tbdata.column("medprice",width=100)
tbdata.column("stock",width=65)
tbdata.column("desc",width=85)
tbdata.column("date",width=98)
tbdata.column("orderid",width=80)
tbdata.pack(fill=BOTH,expand=1)
tbdata.bind("<ButtonRelease-1>",getdata)
showdata()
rt.mainloop()