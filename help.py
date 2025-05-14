import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System - Help Desk")

        # === Background Image ===
        bg_img = Image.open(r"C:\Users\bhati\Desktop\Face Recognition Project\images\helpb1.jpg")
        bg_img = bg_img.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(bg_img)

        bg_label = Label(self.root, image=self.photo_bg)
        bg_label.place(x=0, y=0, width=1530, height=790)

        # === Support Frame ===
        support_frame = Frame(self.root, bg="white", bd=4, relief=RIDGE)
        support_frame.place(x=500, y=300, width=535, height=280)

        # Title
        title_lbl = Label(support_frame, text="Contact Support", font=("Arial", 20, "bold"), bg="white", fg="#0b5394")
        title_lbl.pack(pady=10)

        # Contact Info
        Label(support_frame, text="📧 Email: attendify@gmail.com", font=("Segoe UI", 13), bg="white", fg="blue").pack(anchor="w", padx=30, pady=5)
        Label(support_frame, text="📞 Phone: XXXXXXXXXX", font=("Segoe UI", 13), bg="white", fg="blue").pack(anchor="w", padx=30, pady=5)
        Label(support_frame, text="🕒 Support Hours: 9 AM - 6 PM (Mon - Fri)", font=("Segoe UI", 13), bg="white", fg="blue").pack(anchor="w", padx=30, pady=5)
        Label(support_frame, text="📍 Location: Chitkara University, CSE Dept", font=("Segoe UI", 13), bg="white", fg="blue").pack(anchor="w", padx=30, pady=5)

        # Back to Home Button (inside the frame)
        Button(support_frame, text="Back to Home", font=("Segoe UI", 12, "bold"),
               bg="#0b5394", fg="white", cursor="hand2", command=self.back_to_home).pack(pady=15)

    def back_to_home(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()