
from logging import root
from tkinter import*
from tkinter import messagebox
from turtle import title
import os
from PIL import Image, ImageTk
# import Criminal as cr


class Login2:
    def __init__(self,root):
        self.root=root
        self.root.title("Criminal/LoginPage")
        self.root.geometry("1280x720+100+50")

        # images
             
        # img2=Image.open('images/login2_img.png')
        # img2=img2.resize((550,160),Image.LANCZOS)
        # self.bg=ImageTk.PhotoImage(img2)

        # self.img_2=Label(self.root,image=self.bg)
        # self.img_2.place(x=0,y=0,relwidth=1,relheight=1,width=1550,height=500)


        img=Image.open('images/login2_img.png')
        img=img.resize((1550,800),Image.LANCZOS)
        self.bg=ImageTk.PhotoImage(img)
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # self.bg_image=Label(self.root,image=img2).place(x=0,y=0,relwidth=1,relheight=1)



        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=345,y=210,height=400,width=600)

        title=Label(Frame_login,text="Login",font=("sans-serif",35,"bold"),fg="#d77337",background="white").place(x=220,y=0)

        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",20,"bold"),fg="gray",bg="white").place(x=70,y=120)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=235,y=125,width=300,height=35)

        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",20,"bold"),fg="gray",bg="white").place(x=70,y=200)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_pass.place(x=235,y=205,width=300,height=35)

        Login_btn=Button(Frame_login,command=self.login_fun,text=("Login"),fg="white",bg="#d77337",font=("times new roman",20)).place(x=300,y=300,width=180,height=45)
        



    def login_fun(self):
        if self.txt_pass.get()=="" and self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        elif self.txt_user.get()=="":
            messagebox.showerror("Error","Enter Username",parent=self.root)

        elif self.txt_pass.get()=="":
            messagebox.showerror("Error","Enter Password",parent=self.root)

        elif self.txt_user.get()!="Atish" and self.txt_pass.get()!="admin":
            messagebox.showerror("Invalid","Invalid Username and Password",parent=self.root)

        elif self.txt_user.get()!="Atish" or self.txt_pass.get()!="admin":
            messagebox.showerror("Invalid","Invalid Username/Password",parent=self.root)

        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}",parent=self.root)
            
            self.root.destroy()
            # os.system('Criminal.py')
            
        



root=Tk()
obj=Login2(root)
root.mainloop()

        