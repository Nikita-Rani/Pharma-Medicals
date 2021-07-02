from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

def login_function():
        if txtuser.get()==""or txtpass.get()=="":
            messagebox.showerror("Error","All fields are required")
        # elif self.txtuser.get()!="Nidhi"or self.txtpass.get()!="1002":
        #     messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            user_email=txtuser.get()
            user_pass=txtpass.get()
            try:
                db=mysql.connector.connect(host="localhost",user="root",password="",database="pharma")
                mycursor=db.cursor()
                mycursor.execute("select * from user_info where user_email=%s and user_pass=%s",(user_email,user_pass))
                row=mycursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid UserName and Password")
                else:
                    # print(row)
                    user_role=row[1]
                    # print(user_role)
                    if user_role=="1":
                        # rt.destroy()
                        messagebox.showinfo("Success", "Welcome admin")
                        rt.destroy()
                        import admin
                    elif user_role=="0":
                        messagebox.showinfo("Success","welcome user")
                        rt.destroy()
                        import user
                    # db.commit()
            except EXCEPTION as e:
                 print(e)
            db.rollback()
            db.close()
def regi():
    rt.destroy()
    import register
def forgetpassword():
    import forgetpass
def back():
    rt.destroy()
    import main    
    
rt=Tk()
rt.title("Login System")
rt.geometry("1600x900+0+0")
        #====BG Image=====
photo=Image.open(r"images/loginbg.jpg")
bg=ImageTk.PhotoImage(photo)
lbl_bg=Label(rt,image=bg)
lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
                #====Login Frame=====
frame=Frame(rt,bg="white")
frame.place(x=150,y=150,height=400,width=500)

title=Label(frame,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white")
title.place(x=90,y=30)
desc=Label(frame,text="Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white")
desc.place(x=90,y=100)

img1=Image.open(r"images\loginlogo.jpg")
img1=img1.resize((100,100),Image.ANTIALIAS)
photoimage1=ImageTk.PhotoImage(img1)
lblimg=Label(image=photoimage1,bg="white",borderwidth=0)
lblimg.place(x=480,y=200,width=100,height=100)

                #====label====
username=Label(frame,text="User Email",font=("Goudy old style",15,"bold"),fg="gray",bg="white")
username.place(x=118,y=140)

txtuser=Entry(frame,font=("times new roman",15),bg="lightgray")
txtuser.place(x=90,y=170,width=350,height=35)

password=Label(frame,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white")
password.place(x=118,y=210)

txtpass=Entry(frame,font=("times new roman",15),bg="lightgray")
txtpass.place(x=90,y=240,width=350,height=35)
txtpass.config(show="*")

                #====icon======
img2=Image.open(r"images\userpic.png")
img2=img2.resize((25,25),Image.ANTIALIAS)
photoimage2=ImageTk.PhotoImage(img2)
lblimg1=Label(image=photoimage2,bg="white",borderwidth=0)
lblimg1.place(x=238,y=290,width=25,height=25)

img3=Image.open(r"images\passwordpic.png")
img3=img3.resize((25,25),Image.ANTIALIAS)
photoimage3=ImageTk.PhotoImage(img3)
lblimg2=Label(image=photoimage3,bg="white",borderwidth=0)
lblimg2.place(x=238,y=362,width=25,height=25)

                #loginbutton
loginbtn=Button(frame,command=login_function,text="Login",cursor="hand2",fg="white",bg="#d77337",font=("times new roman",20))
loginbtn.place(x=255,y=290,width=180,height=40)
backbtn=Button(frame,command=back,text="Back",cursor="hand2",fg="white",bg="#d77337",font=("times new roman",20))
backbtn.place(x=258,y=340,width=180,height=40)
                #registerbutton
registerbtn=Button(frame,text="Create New Account",command=regi,cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",13))
registerbtn.place(x=90,y=280)
                #forgetbutton
forgetpass=Button(frame,text="Forget Password?",command=forgetpassword,cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",13))
forgetpass.place(x=90,y=300)

            
                            # messagebox.showinfo("Welcome",f"Welcome {self.txtuser.get()}!\nYou are successfully logged in.")
rt.mainloop()