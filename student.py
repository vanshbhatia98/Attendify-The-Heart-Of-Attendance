import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_section=StringVar()
        self.var_group=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        # Base directory for images
        base_dir = r"images"

        # First Image
        img_path = os.path.join(base_dir, "ab.jpg")
        img = Image.open(img_path)
        img = img.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second Image
        img1_path = os.path.join(base_dir, "bc.jpg")
        img1 = Image.open(img1_path)
        img1 = img1.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Third Image
        img2_path = os.path.join(base_dir, "cd.jpg")
        img2 = Image.open(img2_path)
        img2 = img2.resize((500, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # Background Image
        img3 = Image.open(r"C:\Users\bhati\Desktop\Face Recognition Project\images\background.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)  # Resize the correct image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title label
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # Left label (Student Details)
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=580)

        # Left Image for Left Frame
        img_left = os.path.join(base_dir, "classroom.jpg")
        img_left = Image.open(img_left)
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)  # Resize to fit the frame
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # Current course information
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current course information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=700, height=115)

        #Department

        dep_label = Label(current_course_frame, font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=2)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 13, "bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Engineering","BCA","PHARMACY","NURSING")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 13, "bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","BE-CSE","BCA","B-PHARMACY","NURSING")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman", 13, "bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman", 13, "bold"),width=20,state="readonly")
        semester_combo["values"]=("Select Semester","SEM-1","SEM-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information
        class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        class_Student_frame.place(x=5, y=250, width=700, height=300)

        #student id
        studentId_label = Label(class_Student_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_id,width=20,font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label = Label(class_Student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_name,width=20,font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Section
        class_div_label = Label(class_Student_frame, text="Section:", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10,pady=5,sticky=W)

        # class_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_section,width=20,font=("times new roman", 13, "bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_section,font=("times new roman", 13, "bold"),width=18,state="readonly")
        div_combo["values"]=("Select Section","A","B","C","D","E","F","G","H")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #group
        roll_no_label = Label(class_Student_frame, text="Group:", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10,pady=5,sticky=W)

        # roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_group,width=20,font=("times new roman", 13, "bold"))
        # roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        roll_no_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_group,font=("times new roman", 13, "bold"),width=18,state="readonly")
        roll_no_combo["values"]=("Select Group","1","2")
        roll_no_combo.current(0)
        roll_no_combo.grid(row=1,column=3,padx=10,pady=10,sticky=W)

         #Gender
        gender_label = Label(class_Student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10,pady=5,sticky=W)

        # gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman", 13, "bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman", 13, "bold"),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=0,sticky=W)

         #Dob
        dob_label = Label(class_Student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label = Label(class_Student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman", 13, "bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone No
        phone_label = Label(class_Student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label = Label(class_Student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman", 13, "bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher name
        teacher_label = Label(class_Student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

    
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #buttons frame

        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)
 
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


  

        # Right label Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)

        # Right Image for Right Frame
        img_right = os.path.join(base_dir, "classroom1.jpg")
        img_right = Image.open(img_right)
        img_right = img_right.resize((720, 130), Image.Resampling.LANCZOS)  # Resize to fit the frame
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

    #======== Search System ========
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,
                                text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=710, height=70)

        # “Search By” Label
        search_label = Label(Search_frame, text="Search By:",
                            font=("times new roman", 15, "bold"),
                            bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        # Combobox for field selection
        self.search_by = ttk.Combobox(Search_frame,
                                    font=("times new roman", 13, "bold"),
                                    width=15, state="readonly")
        self.search_by["values"] = ("Select", "StudentId", "Phone")
        self.search_by.current(0)
        self.search_by.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Entry for search text
        self.search_var = StringVar()
        self.search_entry = ttk.Entry(Search_frame, width=15,
                                    font=("times new roman", 13, "bold"),
                                    textvariable=self.search_var)
        self.search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        # Search button
        search_btn = Button(Search_frame, text="Search", width=12,
                            font=("times new roman", 12, "bold"),
                            bg="blue", fg="white",
                            command=self.search_data)
        search_btn.grid(row=0, column=3, padx=4)

        # Show All button
        showAll_btn = Button(Search_frame, text="Show All", width=12,
                            font=("times new roman", 12, "bold"),
                            bg="blue", fg="white",
                            command=self.fetch_data)
        showAll_btn.grid(row=0, column=4, padx=4)


        #table frame
        table_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","section","group","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Dep")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("group",text="Group")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("section",text="Section")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("group",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("section",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #Function Declaration
    def add_data(self):
        # pass  #Placeholder, taki error na aaye
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="@Bhatia98@",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                                                                            
                                                                                            self.var_dep.get(),           
                                                                                            self.var_course.get(),
                                                                                            self.var_year.get(),
                                                                                            self.var_semester.get(),
                                                                                            self.var_id.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_section.get(),
                                                                                            self.var_group.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_teacher.get(),
                                                                                            self.var_radio1.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def search_data(self):
        if self.search_by.get() == "Select" or self.search_var.get().strip() == "":
            messagebox.showerror("Error", "Please select a search option and enter a search term", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="@Bhatia98@", database="face_recognizer"
            )
            my_cursor = conn.cursor()
            field = self.search_by.get()
            term = f"%{self.search_var.get().strip()}%"
            query = f"SELECT * FROM student WHERE {field} LIKE %s"
            my_cursor.execute(query, (term,))
            rows = my_cursor.fetchall()

            self.student_table.delete(*self.student_table.get_children())
            if rows:
                for row in rows:
                    self.student_table.insert("", END, values=row)
            else:
                messagebox.showinfo("No Result", "No matching record found.", parent=self.root)

            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
    #Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="@Bhatia98@",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Get Cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()                
        content=self.student_table.item(cursor_focus)
        data=content["values"]
    
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_section.set(data[6]),
        self.var_group.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    # Update Function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@Bhatia98@", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, StudentId=%s, Name=%s, Section=%s, `Group`=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where StudentId=%s", (
                        self.var_dep.get(),           
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_id.get(),  
                        self.var_name.get(),
                        self.var_section.get(),
                        self.var_group.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details update successfully completed", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)



    #delete data
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@Bhatia98@", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where StudentId=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                    messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)    

    #reset
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_section.set("Select Section"),
        self.var_group.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
                

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@Bhatia98@", database="face_recognizer")
                    my_cursor = conn.cursor()
                    
                    my_cursor.execute("SELECT MAX(StudentId) FROM student")
                    last_id = my_cursor.fetchone()[0]
                    new_id = 1 if last_id is None else last_id + 1  # Ensure unique ID

                    my_cursor.execute("""
                        UPDATE student SET Dep=%s, Course=%s, Year=%s, Semester=%s, StudentId=%s, Name=%s, Section=%s, `Group`=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s 
                        WHERE StudentId=%s
                    """, (
                        self.var_dep.get(),           
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        new_id,  
                        self.var_name.get(),
                        self.var_section.get(),
                        self.var_group.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()  # ✅ Ensure correct ID is used
                    ))

                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # ✅ Fix: Ensure face detection works properly
                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y+h, x:x+w]
                            return face_cropped
                        return None  # Ensure it doesn't break the loop

                    cap = cv2.VideoCapture(0)
                    img_id = 0

                    # ✅ Fix: Ensure folder exists
                    if not os.path.exists("data"):
                        os.makedirs("data")

                    while True:
                        ret, my_frame = cap.read()
                        cropped_face = face_cropped(my_frame)
                        
                        if cropped_face is not None:
                            img_id += 1
                            face = cv2.resize(cropped_face, (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                            file_name_path = f"data/user.{new_id}.{img_id}.jpg"
                            cv2.imwrite(file_name_path, face)

                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                            # ✅ Debug: Ensure images are saving correctly
                            print(f"Saving: {file_name_path}")

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data sets completed successfully..")

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="@Bhatia98@", database="face_recognizer")
                    my_cursor = conn.cursor()
                    
                    # ✅ Fix: Use existing StudentId if available
                    student_id = self.var_id.get()
                    if not student_id:  # If it's a new student, generate new ID
                        my_cursor.execute("SELECT MAX(StudentId) FROM student")
                        last_id = my_cursor.fetchone()[0]
                        student_id = 1 if last_id is None else last_id + 1  
                    
                    # ✅ Fix: Don't change StudentId for existing students
                    my_cursor.execute("""
                        UPDATE student SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, 
                        Section=%s, `Group`=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, 
                        Teacher=%s, PhotoSample=%s WHERE StudentId=%s
                    """, (
                        self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                        self.var_semester.get(), self.var_name.get(), self.var_section.get(),
                        self.var_group.get(), self.var_gender.get(), self.var_dob.get(),
                        self.var_email.get(), self.var_phone.get(), self.var_address.get(),
                        self.var_teacher.get(), self.var_radio1.get(), student_id
                    ))
                    
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    # ✅ Fix: Ensure face detection works properly
                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y+h, x:x+w]
                            return face_cropped
                        return None  

                    cap = cv2.VideoCapture(0)
                    img_id = 0

                    if not os.path.exists("data"):
                        os.makedirs("data")

                    while True:
                        ret, my_frame = cap.read()
                        cropped_face = face_cropped(my_frame)
                        
                        if cropped_face is not None:
                            img_id += 1
                            face = cv2.resize(cropped_face, (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                            file_name_path = f"data/user.{student_id}.{img_id}.jpg"  # ✅ Fix: Use correct Student ID
                            cv2.imwrite(file_name_path, face)

                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                            print(f"Saving: {file_name_path}")

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data sets completed successfully..")

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()

