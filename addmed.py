from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector

def back():
    rt.destroy()
    import admin
    
def add():
    if mednm1.get()=="" or medexp1.get()=="" or medman1.get()=="" or meddecs1.get()==""or medprice1.get()=="" or medst1.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        med_name=mednm1.get()
        med_exp=medexp1.get()
        med_mfd=medman1.get()
        med_price=medprice1.get()
        med_stock=medst1.get()
        med_desc=meddecs1.get()
        db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
        mycursor=db.cursor()
    try:
        sql="insert into med_info(med_name,med_exp,med_mfd,med_price,med_stock,med_desc)values(%s,%s,%s,%s,%s,%s)"
        val=(med_name,med_exp,med_mfd,med_price,med_stock,med_desc)
        mycursor.execute(sql,val)
        db.commit()
        messagebox.showinfo("information","Record Inserted successfully")
        clearall()
        
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()
    showdata()
def update():
    if mednm1.get()=="" or medexp1.get()=="" or medman1.get()=="" or meddecs1.get()==""or medprice1.get()=="" or medst1.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        med_name=mednm1.get()
        med_exp=medexp1.get()
        med_mfd=medman1.get()
        med_price=medprice1.get()
        med_stock=medst1.get()
        med_desc=meddecs1.get()
        db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
        mycursor=db.cursor()
    try:
        sql="update med_info set med_exp=%s,med_mfd=%s,med_price=%s,med_stock=%s,med_desc=%s where med_name=%s"
        val=(med_exp,med_mfd,med_price,med_stock,med_desc,med_name)
        mycursor.execute(sql,val)
        db.commit()
        messagebox.showinfo("information","Record Updated successfully")
        clearall()
        showdata()

        
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()
    # showdata()
# def deleteall():
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
    medexp1.delete(0, END)
    medman1.delete(0, END)
    medprice1.delete(0, END)
    medst1.delete(0, END)
    meddecs1.delete(0, END)
    mednm1.focus_set()
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
            tbdata.insert('',END,values=[row[1:2],row[3:4],row[2:3],row[4:5],row[5:6],row[6]])
        db.commit()
        db.close()
        lsearch.delete(0,END)
        searchbar.delete(0,END)
def showdata():
    med_name=mednm1.get()
    med_exp=medexp1.get()
    med_mfd=medman1.get()
    med_price=medprice1.get()
    med_stock=medst1.get()
    med_desc=meddecs1.get()
    db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
    mycursor=db.cursor()
    mycursor.execute("select * from med_info")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        tbdata.delete(*tbdata.get_children())
    for row in rows:
        tbdata.insert('',END,values=[row[1:2],row[3:4],row[2:3],row[4:5],row[5:6],row[6]])
    db.commit()
    db.close()
def getdata(event):
    currow=tbdata.focus()
    contents=tbdata.item(currow)
    row=contents['values']
    mednm1.delete(0,END)
    medexp1.delete(0, END)
    medman1.delete(0, END)
    medprice1.delete(0, END)
    medst1.delete(0, END)
    meddecs1.delete(0, END)
    mednm1.insert(0,row[0])
    medexp1.insert(0,row[2])
    medman1.insert(0,row[1])
    medprice1.insert(0,row[3])
    medst1.insert(0,row[4])
    meddecs1.insert(0,row[5])
    

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
stitle=Label(sidefrm,text="Medicine Manager",font=("Sitka Text",20,"bold"),fg="#0F5257",bg="#C1CAD6")
stitle.grid(row=0,columnspan=2,pady=10)
mednm=Label(sidefrm,text="Medicine Name",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
mednm.grid(row=1,column=0,padx=20,pady=10,sticky="w")
mednm1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
mednm1.grid(row=1,column=1,padx=20,pady=10,sticky="w")
medexp=Label(sidefrm,text="Expiry Date",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
medexp.grid(row=2,column=0,padx=20,pady=10,sticky="w")
medexp1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medexp1.grid(row=2,column=1,padx=20,pady=10,sticky="w")
medman=Label(sidefrm,text="Manufacture Date",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
medman.grid(row=3,column=0,padx=20,pady=10,sticky="w")
medman1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medman1.grid(row=3,column=1,padx=20,pady=10,sticky="w")
meddesc=Label(sidefrm,text="Description",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
meddesc.grid(row=4,column=0,padx=20,pady=10,sticky="w")
meddecs1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
meddecs1.grid(row=4,column=1,padx=20,pady=10,sticky="w")
medprice=Label(sidefrm,text="Medicine Price",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
medprice.grid(row=5,column=0,padx=20,pady=10,sticky="w")
medprice1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medprice1.grid(row=5,column=1,padx=20,pady=10,sticky="w")
medstock=Label(sidefrm,text="Medicine Stock",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
medstock.grid(row=6,column=0,padx=20,pady=10,sticky="w")
medst1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medst1.grid(row=6,column=1,padx=20,pady=10,sticky="w")

#Buttons
btnframe=Frame(sidefrm,bd=7,relief=RIDGE,bg="darkgray")
btnframe.place(x=15,y=410,width=390,height=70)

addbtn=Button(btnframe,text="ADD ",command=add,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=4,column=0,padx=10,pady=10)
addbtn=Button(btnframe,text="UPDATE",command=update,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=4,column=1,padx=10,pady=10)
# addbtn=Button(btnframe,text="DELETE",command=deleteall,bd=5,relief=RAISED,width=7,font=("System",10,"bold")).grid(row=4,column=2,padx=10,pady=10)
addbtn=Button(btnframe,text="CLEAR",command=clearall,bd=5,relief=RAISED,width=11,font=("System",10,"bold")).grid(row=4,column=3,padx=10,pady=10)


#rightframe
mainfrm=Frame(rt,bd=5,relief=GROOVE,bg="#C1CAD6")
mainfrm.place(x=490,y=100,width=840,height=560)
maintitle=Label(mainfrm,text="Medicine Displayer",font=("Sitka Text",20,"bold"),fg="#0F5257",bg="#C1CAD6")
maintitle.place(x=190,y=10,width=400,height=40)

searchfrm=Frame(mainfrm,bd=5,relief=FLAT,bg="white")
searchfrm.place(x=15,y=70,width=800,height=450)
searchlb=Label(searchfrm,text="Search By",font=("Monotype Corsiva",18,"bold"),bg="white")
searchlb.grid(row=0,column=0,padx=10,pady=10,sticky="w")
searchbar=ttk.Combobox(searchfrm,width=10,font=("Times New Roman",13,"bold"),state="readonly")
# searchbar['values']=("med_id","med_name")
searchbar['values']=("med_name","med_desc")
searchbar.grid(row=0,column=1,padx=20,pady=10)
lsearch=Entry(searchfrm,font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE)
lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")

searchbt=Button(searchfrm,text="SEARCH",command=search,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=4,padx=10,pady=10)
searchbt=Button(searchfrm,text="SHOW ALL",command=showdata,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=5,padx=10,pady=10)

tbframe=Frame(searchfrm,bd=4,relief=RIDGE,bg="#C1CAD6")
tbframe.place(x=20,y=60,width=720,height=360)
scrollx=Scrollbar(tbframe,orient=HORIZONTAL)
scrolly=Scrollbar(tbframe,orient=VERTICAL)
tbdata=ttk.Treeview(tbframe,columns=("mednm","medman","medexp","medprice","stock","desc"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=tbdata.xview)
scrolly.config(command=tbdata.yview)
tbdata.heading("mednm",text="Medicine Name")
tbdata.heading("medman",text="Manufacture Date")
tbdata.heading("medexp",text="Expiry Date")
tbdata.heading("medprice",text="Medicine Price")
tbdata.heading("stock",text="Quantity")
tbdata.heading("desc",text="Description")
tbdata['show']="headings"
tbdata.column("mednm",width=100)
tbdata.column("medman",width=100)
tbdata.column("medexp",width=100)
tbdata.column("medprice",width=100)
tbdata.column("stock",width=100)
tbdata.column("desc",width=100)
tbdata.pack(fill=BOTH,expand=1)
tbdata.bind("<ButtonRelease-1>",getdata)
showdata()
rt.mainloop()