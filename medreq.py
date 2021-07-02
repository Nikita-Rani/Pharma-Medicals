from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import mysql.connector
def back():
    rt.destroy()
    import user

def add():
    if username1.get()=="" or medname1.get()=="" or medadd1.get()=="" or medquan1.get()==""or user_contact1.get()=="" or user_email1.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        user_fname=username1.get()
        med_name=medname1.get()
        del_add=medadd1.get()
        order_quan=medquan1.get()
        order_contact=user_contact1.get()
        order_email=user_email1.get()
        db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
        mycursor=db.cursor()
    try:
        mycursor.execute("select * from user_info where user_fname=%s",(user_fname,))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("Error","Invalid User Name ")
        else:
            user_id=row[0]
            mycursor.execute("select * from med_info where med_name=%s",(med_name,))
            row1=mycursor.fetchone()

            if(row1==None):
                messagebox.showerror("Error","Invalid medicine name ")
            else:
                med_id=row1[0]
                med_price=row1[4]
                med_stock=row1[5]
                print(med_stock)
                if(int(order_quan)>int(med_stock)):
                    messagebox.showerror("Error","medicine out of stock")
                else:
                    order_cost=int(med_price)*int(order_quan)
                    sql="insert into med_order_req(user_id,med_id,del_add,order_quan,order_cost,order_contact,order_email,      order_status,order_date_del)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    val=(user_id,med_id,del_add,order_quan,order_cost,order_contact,order_email,"pending","pending")
                    mycursor.execute(sql,val)
                    db.commit()
                    messagebox.showinfo("information","Succesfully ordered please wait for admin confirmation")
                    clearall()   
    except EXCEPTION as e:
        print(e)
        db.rollback()
        db.close()
    showdata()
    


def viewprice():
    if username1.get()=="" or medname1.get()=="" or medadd1.get()=="" or medquan1.get()==""or user_contact1.get()=="" or user_email1.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        med_name=medname1.get()
        order_quan=medquan1.get()
        try:
            db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
            mycursor=db.cursor()
            mycursor.execute("select * from med_info where med_name=%s",(med_name,))
            row1=mycursor.fetchone()
            if(row1==None):
                messagebox.showerror("Error","Invalid medicine Name ")
            else:
                med_price=row1[4]
                order_cost=int(med_price)*int(order_quan)
                messagebox.showinfo("Info:total price",order_cost)
        except EXCEPTION as e:
        # print(e)
            db.rollback()
            db.close()
        # showdata()

def repeatorder():
    add()
    

    
def clearall():
    username1.delete(0,END)
    medname1.delete(0, END)
    medadd1.delete(0, END)
    medquan1.delete(0, END)
    user_contact1.delete(0, END)
    user_email1.delete(0, END)
    username1.focus_set()
    

# def search():
#     ser1=searchbar.get()
#     lsearch1=lsearch.get()
#     if(lsearch1=="" or ser1==""):
#         messagebox.showerror("Error","Empty Field")
#     else:
#         db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
#         mycursor=db.cursor()
#         mycursor.execute("select * from med_info where "+str(ser1)+" LIKE '%"+str(lsearch1)+"%'")
#         rows=mycursor.fetchone()
#         if len(rows)!=0:
#             tbdata.delete(*tbdata.get_children())
#         elif len(rows)==0:
#             messagebox.showinfo("info","no record found")
#         for row in rows:
#             med_id=row[2]
#             mycursor.execute("select * from med_info where med_id=%s",(med_id,))
#             info=mycursor.fetchone()
#             med_nm=info[1]
#             tbdata.insert('',END,values=[row[2],row[3],row[4],row[5],row[9],row[8]])
#         db.commit()
#         db.close()
#         lsearch.delete(0,END)
#         searchbar.delete(0,END)


def showdata():
    db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
    mycursor=db.cursor()
    mycursor.execute("select * from med_order_req")
    rows=mycursor.fetchall()
    if len(rows)!=0:
        tbdata.delete(*tbdata.get_children())
    for row in rows:
        med_id=row[2]
        mycursor.execute("select * from med_info where med_id=%s",(med_id,))
        info=mycursor.fetchone()
        # print(info)
        med_nm=info[1]
        # print(med_nm)
        tbdata.insert('',END,values=[med_nm,row[3],row[4],row[5],row[9],row[8]])
    db.commit()
    db.close()


def getdata(event):
    currow=tbdata.focus()
    contents=tbdata.item(currow)
    row=contents['values']
    username1.delete(0,END)
    medname1.delete(0, END)
    medadd1.delete(0, END)
    medquan1.delete(0, END)
    user_contact1.delete(0, END)
    user_email1.delete(0, END)
    # username1.insert(0,row[0])
    medname1.insert(0,row[0])
    medadd1.insert(0,row[1])
    medquan1.insert(0,row[2])
    # user_contact1.insert(0,row[4])
    # user_email1.insert(0,row[5])
    

rt=Tk()
rt.geometry("1600x900+0+0")
rt.title("Add Medicine")
title=Label(rt,text="Welcome To Pharma Medicals",bd=8,relief=SUNKEN,font=("Sitka Text",35,"bold"),fg="#66101F",bg="#C1CAD6")
title.pack(side=TOP,fill=X)
backbtn=Button(rt,text="BACK",command=back,bd=5,relief=RAISED,width=7,font=("System",10,"bold"),bg="#755B69",fg="white")
backbtn.place(x=30,y=20,width=90,height=40)
#C1CAD6
sidefrm=Frame(rt,bd=5,relief=GROOVE,bg="#C1CAD6")
sidefrm.place(x=20,y=100,width=450,height=560)
stitle=Label(sidefrm,text="Order Your Medicine",font=("Sitka Text",20,"bold"),fg="#0F5257",bg="#C1CAD6")
stitle.grid(row=0,columnspan=2,pady=10)

username=Label(sidefrm,text="Full Name",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
username.grid(row=1,column=0,padx=20,pady=10,sticky="w")
username1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
username1.grid(row=1,column=1,padx=20,pady=10,sticky="w")

medname=Label(sidefrm,text="Medicine Name",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
medname.grid(row=2,column=0,padx=20,pady=10,sticky="w")
medname1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medname1.grid(row=2,column=1,padx=20,pady=10,sticky="w")

medadd=Label(sidefrm,text="Delievery Address",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
medadd.grid(row=3,column=0,padx=20,pady=10,sticky="w")
medadd1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medadd1.grid(row=3,column=1,padx=20,pady=10,sticky="w")


medquan=Label(sidefrm,text="Quantity Required",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
medquan.grid(row=4,column=0,padx=20,pady=10,sticky="w")
medquan1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
medquan1.grid(row=4,column=1,padx=20,pady=10,sticky="w")


user_contact=Label(sidefrm,text="Contact Number",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
user_contact.grid(row=5,column=0,padx=20,pady=10,sticky="w")
user_contact1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
user_contact1.grid(row=5,column=1,padx=20,pady=10,sticky="w")

user_email=Label(sidefrm,text="Contact Email",font=("Monotype Corsiva",16,"bold"),bg="#C1CAD6")
user_email.grid(row=6,column=0,padx=20,pady=10,sticky="w")
user_email1=Entry(sidefrm,font=("Times New Roman",13,"bold"),bd=5,relief=RAISED)
user_email1.grid(row=6,column=1,padx=20,pady=10,sticky="w")

#Buttons
btnframe=Frame(sidefrm,bd=7,relief=RIDGE,bg="darkgray")
# btnframe.place(x=15,y=410,width=400,height=70)
btnframe.place(x=15,y=429,width=420,height=70)



addbtn=Button(btnframe,text="ADD ",command=add,bd=5,relief=RAISED,width=7,font=("System",10,"bold")).grid(row=4,column=0,padx=10,pady=10)
addbtn=Button(btnframe,text="VIEW PRICE",command=viewprice,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=4,column=1,padx=5,pady=10)
addbtn=Button(btnframe,text="REPEAT ORDER",command=repeatorder,bd=5,relief=RAISED,width=13,font=("System",10,"bold")).grid(row=4,column=2,padx=5,pady=10)
addbtn=Button(btnframe,text="CLEAR",command=clearall,bd=5,relief=RAISED,width=7,font=("System",10,"bold")).grid(row=4,column=3,padx=2,pady=10)


#rightframe
mainfrm=Frame(rt,bd=5,relief=GROOVE,bg="#C1CAD6")
mainfrm.place(x=490,y=100,width=840,height=560)
maintitle=Label(mainfrm,text="Your Order History",font=("Sitka Text",20,"bold"),fg="#0F5257",bg="#C1CAD6")
maintitle.place(x=190,y=10,width=400,height=40)

searchfrm=Frame(mainfrm,bd=5,relief=FLAT,bg="white")
searchfrm.place(x=15,y=70,width=800,height=450)
# searchlb=Label(searchfrm,text="Search By",font=("Monotype Corsiva",18,"bold"),bg="white")
# searchlb.grid(row=0,column=0,padx=10,pady=10,sticky="w")
# searchbar=ttk.Combobox(searchfrm,width=10,font=("Times New Roman",13,"bold"),state="readonly")
# # searchbar['values']=("med_id","med_name")
# searchbar['values']=("med_name",)
# searchbar.grid(row=0,column=1,padx=20,pady=10)
# lsearch=Entry(searchfrm,font=("Times New Roman",15,"bold"),bd=3,relief=RIDGE)
# lsearch.grid(row=0,column=2,pady=10,padx=20,sticky="w")

# searchbt=Button(searchfrm,text="SEARCH",command=search,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=4,padx=10,pady=10)
# searchbt=Button(searchfrm,text="SHOW ALL",command=showdata,bd=5,relief=RAISED,width=10,font=("System",10,"bold")).grid(row=0,column=5,padx=10,pady=10)

tbframe=Frame(searchfrm,bd=4,relief=RIDGE,bg="#C1CAD6")
tbframe.place(x=20,y=60,width=720,height=360)
scrollx=Scrollbar(tbframe,orient=HORIZONTAL)
scrolly=Scrollbar(tbframe,orient=VERTICAL)
tbdata=ttk.Treeview(tbframe,columns=("mednm","medadd","medquan","medprice","dod","status"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=tbdata.xview)
scrolly.config(command=tbdata.yview)
tbdata.heading("mednm",text="Medicine Name")
tbdata.heading("medadd",text="Delievery Address")
tbdata.heading("medquan",text="Quantity")
tbdata.heading("medprice",text="Total Price")
tbdata.heading("dod",text="Expected Delievery Date")
tbdata.heading("status",text="Status")
tbdata['show']="headings"
tbdata.column("mednm",width=100)
tbdata.column("medadd",width=100)
tbdata.column("medquan",width=100)
tbdata.column("medprice",width=100)
tbdata.column("dod",width=150)
tbdata.column("status",width=100)
tbdata.pack(fill=BOTH,expand=1)
tbdata.bind("<ButtonRelease-1>",getdata)
showdata()
rt.mainloop()