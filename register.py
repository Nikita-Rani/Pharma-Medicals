from tkinter import*
import mysql.connector
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk 


# class Register:
#     def __init__(self,root):
#         self.root=root
#         self.root.title("REGISTER")
#         self.root.geometry("1600x900+0+0")


        
        
        
        
#         self.bg=ImageTk.PhotoImage(file=r"images\1621446.jpg")
#         bg_lbl=Label(self.root,image=self.bg)
#         bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


#         frame=Frame(self.root,bg="white")
#         frame.place(x=520,y=100,width=800,height=550)

#         register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="blue",bg="light blue")
#         register_lbl.place(x=20,y=20)
        
#         fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
#         fname.place(x=50,y=100)

#         self.fname_entry=ttk.Entry(frame,font=("times new roman",15,"bold"))
#         self.fname_entry.place(x=50,y=130,width=250)

#         l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
#         l_name.place(x=390,y=100)
        
#         self.txt_lname=ttk.Entry(frame,font=("times new roman",15))
#         self.txt_lname.place(x=390,y=130,width=250)
# #..........................row2
#         contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
#         contact.place(x=50,y=170)
        
#         self.txt_contact=ttk.Entry(frame,font=("times new roman",15))
#         self.txt_contact.place(x=50,y=200,width=250)

#         email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
#         email.place(x=390,y=170)
#         self.txt_email=ttk.Entry(frame,font=("times new roman",15))
#         self.txt_email.place(x=390,y=200,width=250)
#         choose=Label(frame,text="Choices",font=("times new roman",15,"bold"),bg="white",fg="black")
#         choose.place(x=50,y=240)
#         self.combo=ttk.Combobox(frame,font=("times new roman",15,"bold"),state="readonly")
#         self.combo["values"]=("Select","User","Admin")
#         self.combo.place(x=50,y=270,width=250)
#         self.combo.current(0)
#         pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
#         pswd.place(x=50,y=310)
#         self.txt_pswd=ttk.Entry(frame,font=("times new roman",15))
#         self.txt_pswd.place(x=50,y=340,width=250)
#         cpswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
#         cpswd.place(x=390,y=310)
#         self.txt_cpswd=ttk.Entry(frame,font=("times new roman",15))
#         self.txt_cpswd.place(x=390,y=340,width=250)
#         #..........checkbutton..........
#         self.vag=IntVar()
#         checkbtn=Checkbutton(frame,variable=self.vag,text="I Agree The Terms & condition",font=("times new roman",11,"bold"),onvalue=1,offvalue=0)
#         checkbtn.place(x=50,y=380)

#         #.............buttons...........
#         img=Image.open(r"images\registerbutton.png")
#         img=img.resize((200,50),Image.ANTIALIAS)
#         self.photoimage=ImageTk.PhotoImage(img)
#         b1=Button(frame,image=self.photoimage,command=self.register,borderwidth=0,cursor="hand2")
#         b1.place(x=10,y=420,width=200)

    
    

root=Tk()
root=root
root.title("REGISTER")
root.geometry("1600x900+0+0")
def back():
    root.destroy()
    import main

def register():
    if fname_entry.get()==""or txt_lname.get()=="" or txt_contact.get()=="" or txt_email.get()=="" or txt_pswd.get()=="" or txt_cpswd.get()=="" or combo.get()=="":
        messagebox.showerror("Error","All fields are required",parent=root)
    elif txt_pswd.get()!=txt_cpswd.get():
        messagebox.showerror("Error", "Password and confirm password must be same")
    elif vag.get()==0:
        messagebox.showerror("Error", "please agree our term and condition")
    else:
        user_fname=fname_entry.get()
        user_lname=txt_lname.get()
        user_contact=txt_contact.get()
        user_email=txt_email.get()
        user_pass=txt_pswd.get()
        role=combo.get()
        print(role)
        if role=="Admin":
            user_role="1"
        else:
            user_role='0'
        db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
        mycursor=db.cursor()
        try:
            sql="insert into user_info(user_role,user_fname,user_lname,user_contact,user_email,user_pass)values(%s,%s,%s,%s,%s,%s)"
            val=(user_role,user_fname,user_lname,user_contact,user_email,user_pass)
            mycursor.execute(sql,val)
            db.commit()
            lastid=mycursor.lastrowid
            messagebox.showinfo("information","Record Inserted successfully")
            fname_entry.delete(0,END)
            txt_lname.delete(0, END)
            txt_contact.delete(0, END)
            txt_email.delete(0, END)
            txt_pswd.delete(0, END)
            txt_cpswd.delete(0, END)
        except EXCEPTION as e:
            print(e)
            db.rollback()
            db.close()


        
        
        
photo=Image.open(r"images/medicineback1.jpg")        
bg=ImageTk.PhotoImage(photo)
bg_lbl=Label(root,image=bg)
bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

# frm1=Frame(root,bd=5,relief=RIDGE,bg="white")
# frm1.place(x=200,y=60,width=1000,height=600)
# photo1=Image.open(r"images/medicineback.jpg")      
# bg1=ImageTk.PhotoImage(photo1)
# bg_lbl1=Label(frm1,image=bg1)
# bg_lbl1.place(x=0,y=0,relwidth=1,relheight=1)


frame=Frame(root,bg="white",bd=5,relief=RIDGE)
frame.place(x=230,y=55,width=900,height=600)
photo1=Image.open(r"images/regi.jpg")        
bg1=ImageTk.PhotoImage(photo1)
bg_lbl1=Label(frame,image=bg1)
bg_lbl1.place(x=0,y=0,relwidth=1,relheight=1)


register_lbl=Label(frame,text="REGISTER HERE",font=("Sitka Text",17,"bold"),fg="white",bg="#cb0000")
register_lbl.place(x=90,y=40)

frm1=Frame(frame,bd=5,relief=RIDGE,bg="white") 
frm1.place(x=90,y=100,width=670,height=400)

fname=Label(frm1,text="First Name",font=("times new roman",15,"bold"),bg="white")
fname.place(x=40,y=15)


fname_entry=ttk.Entry(frm1,font=("times new roman",15,"bold"))
fname_entry.place(x=40,y=45,width=250)

l_name=Label(frm1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
l_name.place(x=350,y=15)
        
txt_lname=ttk.Entry(frm1,font=("times new roman",15))
txt_lname.place(x=350,y=45,width=250)
#..........................row2
contact=Label(frm1,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
contact.place(x=40,y=100)
        
txt_contact=ttk.Entry(frm1,font=("times new roman",15))
txt_contact.place(x=40,y=130,width=250)

email=Label(frm1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
email.place(x=350,y=100)
txt_email=ttk.Entry(frm1,font=("times new roman",15))
txt_email.place(x=350,y=130,width=250)

choose=Label(frm1,text="Choices",font=("times new roman",15,"bold"),bg="white",fg="black")
choose.place(x=40,y=170)
combo=ttk.Combobox(frm1,font=("times new roman",15,"bold"),state="readonly")
combo["values"]=("Select","User","Admin")
combo.place(x=40,y=200,width=250)
combo.current(0)
pswd=Label(frm1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
pswd.place(x=350,y=170)
txt_pswd=ttk.Entry(frm1,font=("times new roman",15))
txt_pswd.place(x=350,y=200,width=250)
txt_pswd.config(show="*")
cpswd=Label(frm1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
cpswd.place(x=350,y=250)
txt_cpswd=ttk.Entry(frm1,font=("times new roman",15))
txt_cpswd.place(x=350,y=280,width=250)
txt_cpswd.config(show="*")

#..........checkbutton..........
vag=IntVar()
checkbtn=Checkbutton(frm1,variable=vag,text="I Agree The Terms & Condition",font=("times new roman",11,"bold"),onvalue=1,offvalue=0)
checkbtn.place(x=40,y=280)
#.............buttons...........
img=Image.open(r"images/registerbtn.jpg")
img=img.resize((160,50),Image.ANTIALIAS)
photoimage1=ImageTk.PhotoImage(img)
b1=Button(frm1,image=photoimage1,command=register,borderwidth=0,cursor="hand2")
b1.place(x=250,y=330,width=150)

backbtn=Button(frame,text="BACK",command=back,bd=5,relief=RAISED,width=7,font=("System",10,"bold"),fg="white",bg="#cb0000")
backbtn.place(x=680,y=40,width=90,height=40)
root.mainloop()
        
        
# bg="#A7C7E7",fg="#393E41"




            







# if __name__=="__main__":
#     root=Tk()
#     app=Register(root)
#     root.mainloop()