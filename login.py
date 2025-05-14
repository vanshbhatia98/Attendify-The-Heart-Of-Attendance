from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from main import Face_Recognition_System
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")


        self.bg=ImageTk.PhotoImage(file=r"C:\Users\bhati\Desktop\Face Recognition Project\images\loginn.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        #Frame
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        # from PIL import Image, ImageTk
        img1 = Image.open(r"C:\Users\bhati\Desktop\Face Recognition Project\images\loggicon.jpg")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimage1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimage1.place(x=730, y=175, width=90, height=90)

        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=85)


        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("times new roman",20,"bold"))
        self.txtpass.place(x=40,y=250,width=270)


        #*****************Icon Images ****************
        img2 = Image.open(r"C:\Users\bhati\Desktop\Face Recognition Project\images\loggicon.jpg")
        img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimage1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimage1.place(x=650, y=325, width=25, height=25)

        #Password
        img3 = Image.open(r"C:\Users\bhati\Desktop\Face Recognition Project\images\passicon.jpg")
        img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimage1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimage1.place(x=650, y=395, width=25, height=25)


        #login button
        loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        # register Button
        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=350,width=160)

        # forgot password
        forgotbtn=Button(frame,text="Forgot Password",command=self.forget_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=10,y=370,width=160)


    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required!!")
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success", "Welcome to Attendify: The Heart of Attendance")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="@Bhatia98@", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (
                    self.txtuser.get(),
                    self.txtpass.get()
                ))
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username & Password")
                else:
                    open_main = messagebox.askyesno("Access Confirmation", "Access only for Admin. Continue?")
                    if open_main:
                        self.new_window = Toplevel(self.root)
                        self.app = Face_Recognition_System(self.new_window)
                conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Database Error: {str(e)}")

    def forget_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter your email to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="@Bhatia98@", database="face_recognizer")
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter a valid email")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                
                Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red", bg="white").place(x=0, y=10, relwidth=1)
                
                Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=80)
                
                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend Name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)
                
                Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=150)
                
                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)
                
                Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="black").place(x=50, y=220)
                
                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15, "bold"), show="*")
                self.txt_newpass.place(x=50, y=250, width=250)
                
                self.email_for_reset = self.txtuser.get()
                
                Button(self.root2, text="Reset", font=("times new roman", 15, "bold"), fg="white", bg="green", command=self.reset_pass).place(x=100, y=290)

    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select Security Question")
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer")
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Error", "Please enter the new password")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="@Bhatia98@", database="face_recognizer")
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s AND securityQ=%s AND securityA=%s"
                value = (self.email_for_reset, self.combo_security_Q.get(), self.txt_security.get())
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Incorrect security answer")
                else:
                    update_query = "UPDATE register SET password=%s WHERE email=%s"
                    update_value = (self.txt_newpass.get(), self.email_for_reset)
                    my_cursor.execute(update_query, update_value)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Your password has been reset. Please log in with the new password.")
                    self.root2.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Database Error: {str(e)}")

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ************** Variables **************
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ************** Background Images **************
        self.bg_image = Image.open(r"C:\Users\bhati\Desktop\Face Recognition Project\images\rejistrbg.jpg")
        self.bg_image = self.bg_image.resize((1600, 900), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg_image)

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\bhati\Desktop\Face Recognition Project\images\images\registrbg.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # ************** Main Frame **************
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # ************** Labels and Entries **************
        Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=100)
        ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold")).place(x=50, y=130, width=250)

        Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=100)
        ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold")).place(x=370, y=130, width=250)

        Label(frame, text="Contact No.", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=170)
        ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15)).place(x=50, y=200, width=250)

        Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=170)
        ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15)).place(x=370, y=200, width=250)

        Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend Name", "Your Pet Name")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50, y=270, width=250)

        Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=240)
        ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new roman", 15)).place(x=370, y=270, width=250)

        Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=310)
        ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*").place(x=50, y=340, width=250)

        Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=310)
        ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show="*").place(x=370, y=340, width=250)

        # ************** Check Button **************
        self.var_check = IntVar()
        Checkbutton(frame, variable=self.var_check, text="I Agree to the Terms & Conditions", font=("times new roman", 12, "bold"), bg="white", onvalue=1, offvalue=0).place(x=50, y=380)

        # ************** Buttons **************
        img_reg = Image.open(r"C:\Users\bhati\Desktop\Face Recognition Project\images\images\registrriconn.jpg")
        img_reg = img_reg.resize((200, 50), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img_reg)

        Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2", bg="white").place(x=10, y=420, width=300)

    # ************** Register Function **************
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required!!")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="@Bhatia98@",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM register WHERE email=%s", (self.var_email.get(),))
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exists, try another email")
                else:
                    my_cursor.execute(
                        "INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_securityQ.get(),
                            self.var_SecurityA.get(),
                            self.var_pass.get()
                        )
                    )
                    conn.commit()
                    messagebox.showinfo("Success", "Registered Successfully")
                conn.close()
            except Exception as es:
                messagebox.showerror("Database Error", f"Error: {str(es)}")
        
if __name__ == "__main__":
    main()



















































