from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

root=Tk()
root.title("Forget Password")
root.geometry("340x390+610+170")

l=Label(root,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
l.place(x=0,y=10,relwidth=1)

enter_email=Label(root,text="Email ID",font=("times new roman",15,"bold"),bg="white",fg="black")
enter_email.place(x=50,y=80)

txt_security_Q=ttk.Entry(root,font=("times new roman",15,"bold"))
txt_security_Q.place(x=50,y=110,width=250)

pass_reset=Label(root,text="Reset Password",font=("times new roman",15,"bold"),bg="white",fg="black")
pass_reset.place(x=50,y=150)

txt_security_Q=ttk.Entry(root,font=("times new roman",15,"bold"))
txt_security_Q.place(x=50,y=180,width=250)

new_password=Label(root,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
new_password.place(x=50,y=220)

txt_security_Q=ttk.Entry(root,font=("times new roman",15,"bold"))
txt_security_Q.place(x=50,y=250,width=250)

btn=Button(root,text="Reset",cursor="hand2",bg="green",fg="white",bd=0,font=("times new roman",12))
btn.place(x=85,y=290,width=180)
root.mainloop()