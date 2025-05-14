import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")

        #Variables
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_sec=StringVar()
        self.var_atten_grp=StringVar()
        self.var_atten_email=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        # Base directory for images
        base_dir = r"images"
        # First Image
        img_path = os.path.join(base_dir, "ab2.jpg")
        img = Image.open(img_path)
        img = img.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # Second Image
        img1_path = os.path.join(base_dir, "abutton.jpg")
        img1 = Image.open(img1_path)
        img1 = img1.resize((800, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # Background Image
        img3 = Image.open(r"images\background.jpg")
        img3 = img3.resize((1530, 710), Image.Resampling.LANCZOS)  # Resize the correct image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        # Title label
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2,bg="white")
        main_frame.place(x=20, y=50, width=1480, height=600)

        # Left label (Student Details)
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=580)

        # Left Image for Left Frame
        img_left = os.path.join(base_dir, "abutton2.jpg")
        img_left = Image.open(img_left)
        img_left = img_left.resize((720, 130), Image.Resampling.LANCZOS)  # Resize to fit the frame
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside_frame = LabelFrame(Left_frame, bd=2,relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=300)

        #Labels and entry
        # #attendance id
        # attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13, "bold"), bg="white")
        # attendanceId_label.grid(row=0, column=0, padx=10,pady=5,sticky=W)

        # attendanceId_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman", 13, "bold"))
        # attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student ID
        rollLabel= Label(left_inside_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg="white")
        rollLabel.grid(row=0, column=0, padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman", 13, "bold"))
        atten_roll.grid(row=0,column=1,pady=8)


        #Name

        nameLabel=Label(left_inside_frame, text="Name:",bg="white", font="comicsansns 11 bold")

        nameLabel.grid(row=0,column=2)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name, font="comicsansns 11 bold")

        atten_name.grid(row=0,column=3,pady=8)

        #Section

        secLabel=Label(left_inside_frame,text="Section:", bg="white", font="comicsansns 11 bold")

        secLabel.grid(row=1,column=0)

        atten_sec=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_sec, font="comicsansns 11 bold")

        atten_sec.grid(row=1,column=1, pady=8)

        #Group

        grpLabel=Label(left_inside_frame, text="Group:",bg="white", font="comicsansns 11 bold")

        grpLabel.grid(row=1,column=2)

        atten_grp=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_grp, font="comicsansns 11 bold")

        atten_grp.grid(row=1,column=3,pady=8)

        #Email

        emailLabel=Label(left_inside_frame, text="Email ID:", bg="white", font="comicsansns 11 bold")

        emailLabel.grid(row=2,column=0)

        atten_email=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_email, font="comicsansns 11 bold")

        atten_email.grid(row=2,column=1,pady=8)


        #time

        timeLabel=Label(left_inside_frame, text="Time:",bg="white", font="comicsansns 11 bold")

        timeLabel.grid(row=2,column=2)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time, font="comicsansns 11 bold")

        atten_time.grid(row=2,column=3,pady=8)

        #Date

        dateLabel=Label(left_inside_frame, text="Date:", bg="white", font="comicsansns 11 bold")

        dateLabel.grid(row=3,column=0)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date, font="comicsansns 11 bold")

        atten_date.grid(row=3,column=1,pady=8)

        #attendance

        attendanceLabel=Label(left_inside_frame, text="Attendance Status", bg="white", font="comicsansns 11 bold")

        attendanceLabel.grid(row=3,column=2)

        self.atten_status=ttk.Combobox(left_inside_frame, width=20,textvariable=self.var_atten_attendance, font="comicsansns 11 bold", state="readonly")

        self.atten_status["values"]=("Status", "Present", "Absent")

        self.atten_status.grid(row=3,column=3,pady=8)

        self.atten_status.current(0)

        #buttons frame

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=10,y=250,width=715,height=50)

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman", 13, "bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

       

        # Right label Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)


        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        #Scroll Bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("Student ID","Student Name","Section","Group","Email ID","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # self.AttendanceReportTable.heading("Attendance ID",text="Attendance ID")
        self.AttendanceReportTable.heading("Student ID",text="Student ID")
        self.AttendanceReportTable.heading("Student Name",text="Student Name")
        self.AttendanceReportTable.heading("Section",text="Section")
        self.AttendanceReportTable.heading("Group",text="Group")
        self.AttendanceReportTable.heading("Email ID",text="Email ID")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"

        # self.AttendanceReportTable.column("Attendance ID",width=100)
        self.AttendanceReportTable.column("Student ID",width=100)
        self.AttendanceReportTable.column("Student Name",width=100)
        self.AttendanceReportTable.column("Section",width=100)
        self.AttendanceReportTable.column("Group",width=100)
        self.AttendanceReportTable.column("Email ID",width=300)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)



    #Fetch Data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
        
    #import csv
    # def importCsv(self):
    #     global mydata
    #     mydata.clear()
    #     fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
    #     with open(fln) as myfile:
    #         csvread=csv.reader(myfile,delimiter=",")
    #         for i in csvread:
    #             mydata.append(i)
    #         self.fetchData(mydata)

    def importCsv(self):
        global mydata
        mydata.clear()
        
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                        filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)

        if not fln:  # If user cancels file selection
            return

        self.csv_file_path = fln  # Save the file path

        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


        self.csv_file_path = fln  # Save the file path globally


    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data is exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_atten_roll.set(row[0])
        self.var_atten_name.set(row[1])
        self.var_atten_sec.set(row[2])
        self.var_atten_grp.set(row[3])
        self.var_atten_email.set(row[4])
        self.var_atten_time.set(row[5])
        self.var_atten_date.set(row[6])
        self.var_atten_attendance.set(row[7])

    def reset_data(self):
        self.var_atten_name.set("")
        self.var_atten_sec.set("")
        self.var_atten_roll.set("")
        self.var_atten_grp.set("")
        self.var_atten_email.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


    #     # Update function
    # def update_data(self):
    #     selected_item = self.AttendanceReportTable.focus()  # Get selected row
    #     if not selected_item:
    #         messagebox.showerror("Error", "No record selected to update!", parent=self.root)
    #         return

    #     # Get updated values from the form
    #     updated_values = [
    #         self.var_atten_roll.get(),
    #         self.var_atten_name.get(),
    #         self.var_atten_sec.get(),
    #         self.var_atten_grp.get(),
    #         self.var_atten_email.get(),
    #         self.var_atten_time.get(),
    #         self.var_atten_date.get(),
    #         self.var_atten_attendance.get(),
    #     ]

    #     # Ensure no empty fields (Optional)
    #     if "" in updated_values:
    #         messagebox.showerror("Error", "All fields must be filled!", parent=self.root)
    #         return

    #     # Update the selected row
    #     self.AttendanceReportTable.item(selected_item, values=updated_values)
    #     messagebox.showinfo("Success", "Record updated successfully!", parent=self.root)

    # # # Link Update button to update_data function
    # # update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17,
    # #                     font=("times new roman", 13, "bold"), bg="blue", fg="white")
    # # update_btn.grid(row=0, column=2)

    def update_data(self):
        selected_item = self.AttendanceReportTable.focus()  # Get selected row
        if not selected_item:
            messagebox.showerror("Error", "No record selected to update!", parent=self.root)
            return

        # Get updated values from the form fields
        updated_values = [
            self.var_atten_roll.get(),
            self.var_atten_name.get(),
            self.var_atten_sec.get(),
            self.var_atten_grp.get(),
            self.var_atten_email.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get(),
        ]

        # Ensure no empty fields (Optional)
        if "" in updated_values:
            messagebox.showerror("Error", "All fields must be filled!", parent=self.root)
            return

        # Update the selected row in Treeview
        self.AttendanceReportTable.item(selected_item, values=updated_values)
        
        # Update CSV file after modification
        self.save_updated_csv()

        messagebox.showinfo("Success", "Record updated successfully & CSV file updated!", parent=self.root)

    # Function to save updated data to CSV
    # def save_updated_csv(self):
    #     # Get all data from Treeview
    #     rows = self.AttendanceReportTable.get_children()
    #     updated_data = [self.AttendanceReportTable.item(row)['values'] for row in rows]

    #     # Overwrite the existing CSV file with updated data
    #     if updated_data:
    #         csv_file_path = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save Updated CSV",
    #                                                     filetypes=(("CSV File", "*.csv"), ("ALL Files", "*.*")), parent=self.root,
    #                                                     defaultextension=".csv")
    #         if csv_file_path:  # If user selects a file
    #             with open(csv_file_path, mode="w", newline="") as file:
    #                 writer = csv.writer(file, delimiter=",")
    #                 writer.writerow(["Student ID", "Student Name", "Section", "Group", "Email ID", "Time", "Date", "Attendance"])  # Column Headers
                    # writer.writerows(updated_data)  # Write updated data


    # def save_updated_csv(self):
    #     if not hasattr(self, 'csv_file_path') or not self.csv_file_path:
    #         messagebox.showerror("Error", "No CSV file imported. Please import a CSV first!", parent=self.root)
    #         return

    #     # Collect all rows from the Treeview
    #     rows = self.AttendanceReportTable.get_children()
    #     updated_data = [self.AttendanceReportTable.item(row)['values'] for row in rows]

    #     # Check if data is available
    #     if not updated_data:
    #         messagebox.showerror("Error", "No data available to save!", parent=self.root)
    #         return

    #     # Open CSV in write mode and update data
    #     with open(self.csv_file_path, mode="w", newline="") as file:
    #         writer = csv.writer(file, delimiter=",")

    #         # Write headers (only once)
    #         writer.writerow(["Student ID", "Student Name", "Section", "Group", "Email ID", "Time", "Date", "Attendance"])

    #         # Write updated rows
    #         writer.writerows(updated_data)

    #     messagebox.showinfo("Success", "CSV file updated successfully!", parent=self.root)


    # def save_updated_csv(self):
    #     if not hasattr(self, 'csv_file_path') or not self.csv_file_path:
    #         messagebox.showerror("Error", "No CSV file imported. Please import a CSV first!", parent=self.root)
    #         return

    #     # Collect all rows from the Treeview
    #     rows = self.AttendanceReportTable.get_children()
    #     updated_data = [self.AttendanceReportTable.item(row)['values'] for row in rows]

    #     # Check if data is available
    #     if not updated_data:
    #         messagebox.showerror("Error", "No data available to save!", parent=self.root)
    #         return

    #     # Open CSV in write mode (overwrite existing data)
    #     with open(self.csv_file_path, mode="w", newline="") as file:
    #         writer = csv.writer(file, delimiter=",")

    #         # **Header sirf tab likhein jab file empty ho**
    #         if file.tell() == 0:
    #             writer.writerow(["Student ID", "Student Name", "Section", "Group", "Email ID", "Time", "Date", "Attendance"])

    #         # Write updated rows
    #         writer.writerows(updated_data)

    #     messagebox.showinfo("Success", "CSV file updated successfully!", parent=self.root)


    def save_updated_csv(self):
        if not hasattr(self, 'csv_file_path') or not self.csv_file_path:
            messagebox.showerror("Error", "No CSV file imported. Please import a CSV first!", parent=self.root)
            return

        # Collect all rows from the Treeview (jo table me dikha raha hai)
        rows = self.AttendanceReportTable.get_children()
        updated_data = [self.AttendanceReportTable.item(row)['values'] for row in rows]

        # Check if data is available
        if not updated_data:
            messagebox.showerror("Error", "No data available to save!", parent=self.root)
            return

        # **File ko "w" (write) mode me open kare taaki purana data overwrite ho**
        with open(self.csv_file_path, mode="w", newline="") as file:
            writer = csv.writer(file, delimiter=",")

            # **Header sirf ek baar likhein (file overwrite hone ke baad)**
            # writer.writerow(["Student ID", "Student Name", "Section", "Group", "Email ID", "Time", "Date", "Attendance"])

            # **Sare updated rows likhein**
            writer.writerows(updated_data)

        messagebox.showinfo("Success", "CSV file updated successfully!", parent=self.root)







if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()