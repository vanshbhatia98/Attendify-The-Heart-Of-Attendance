import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import threading


# Base directory for images
base_dir = r"images"
class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")

        # Title label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        #1st image
        img_top = os.path.join(base_dir, "face_detector3.jpg")
        img_top = Image.open(img_top)
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)  # Resize to fit the frame
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)


        #2nd image
        img_bottom = os.path.join(base_dir, "face_detector2.jpg")
        img_bottom = Image.open(img_bottom)
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)  # Resize to fit the frame
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)


        #button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.start_face_recognition,font=("times new roman", 18, "bold"), bg="darkgreen", fg="WHITE")
        b1_1.place(x=400,y=620,width=200,height=40)
    
    
    
    
    #Attendence
    def mark_attendance(self,s,n,i,j,k):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((s not in name_list) and (n not in name_list) and (i not in name_list) and (j not in name_list) and (k not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d-%m-%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{s},{n},{i},{j},{k},{dtString},{d1},Present")




    #face recognition
    def start_face_recognition(self):
    # This method runs the face recognition in a separate thread
        thread = threading.Thread(target=self.face_recognition)
        thread.daemon = True  # Daemon threads will stop when the main program exits
        thread.start()

    def face_recognition(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="@Bhatia98@", database="face_recognizer")
                my_cursor = conn.cursor()


                # my_cursor.execute("select Name from student where StudentId="+str(id))
                # n=my_cursor.fetchone()
                # n="+".join(n)

                # # my_cursor.execute("select StudentId from student where StudentId="+str(id))
                # # s=my_cursor.fetchone()
                # # s="+".join(s)
                # my_cursor.execute("select StudentId from student where StudentId=" + str(id))
                # s = my_cursor.fetchone()
                # s = str(s[0])  # Directly access and convert to string


                # my_cursor.execute("select Section from student where StudentId="+str(id))
                # i=my_cursor.fetchone()
                # i="+".join(i)

                

                # my_cursor.execute("select Group from student where StudentId="+str(id))
                # j=my_cursor.fetchone()
                # j="+".join(j)

                # my_cursor.execute("select Email from student where StudentId="+str(id))
                # k=my_cursor.fetchone()
                # k="+".join(k)



                my_cursor.execute(f"SELECT Name, StudentId, Section, `Group`, Email FROM student WHERE StudentId={id}")
                result = my_cursor.fetchone()

                if result:
                    n, s, i, j, k = map(str, result)  # Saari values ko string me convert kar diya
                else:
                    n, s, i, j, k = "Unknown", "Unknown", "Unknown", "N/A", "N/A"  # Default values agar record nahi mila




                # if confidence>77:
                #     cv2.putText(img,f"StudentId:{s}",(x,y-100),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     cv2.putText(img,f"Name:{n}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     cv2.putText(img,f"Section:{i}",(x,y-50),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     cv2.putText(img,f"Group:{j}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                #     cv2.putText(img,f"Enail:{k}",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                # if confidence > 77:
                #     text_x = x + w + 10  # Face ke right side me thoda gap de diya
                #     text_y = y - 10 if y - 100 > 0 else y + h + 10  # Agar top pe jagah nahi hai toh neeche shift hoga
                    
                #     cv2.putText(img, f"ID: {s}", (text_x, text_y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                #     cv2.putText(img, f"Name: {n}", (text_x, text_y + 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                #     cv2.putText(img, f"Section: {i}", (text_x, text_y + 60), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                #     cv2.putText(img, f"Group: {j}", (text_x, text_y + 90), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                #     cv2.putText(img, f"Email: {k}", (text_x, text_y + 120), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                if confidence > 77:
                    text_y = y - 10 if y > 50 else y + h + 10  # Agar top pe jagah kam hai toh neeche shift hoga
                    
                    cv2.putText(img, f"ID: {s}", (x, text_y - 100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {n}", (x, text_y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Section: {i}", (x, text_y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Group: {j}", (x, text_y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Email: {k}", (x, text_y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(s,n,i,j,k)



                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            # cv2.imshow("Welcome To Face Recognition",img)
            cv2.imshow("Welcome To Face Recognition", img)
            cv2.waitKey(1)  # This should give the window time to render.


            # if cv2.waitKey(1)==13:
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()





# import os
# from tkinter import *
# from PIL import Image, ImageTk
# import mysql.connector
# import cv2
# import threading

# # Base directory for images
# base_dir = r"images"

# class Face_Recognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognition System")

#         # Title label
#         title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="white", fg="green")
#         title_lbl.place(x=0, y=0, width=1530, height=45)

#         # 1st image
#         img_top = Image.open(os.path.join(base_dir, "face_detector3.jpg"))
#         img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
#         self.photoimg_top = ImageTk.PhotoImage(img_top)
#         f_lbl = Label(self.root, image=self.photoimg_top)
#         f_lbl.place(x=0, y=55, width=650, height=700)

#         # 2nd image
#         img_bottom = Image.open(os.path.join(base_dir, "face_detector2.jpg"))
#         img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
#         self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
#         f_lbl = Label(self.root, image=self.photoimg_bottom)
#         f_lbl.place(x=650, y=55, width=950, height=700)

#         # Button
#         b1_1 = Button(f_lbl, text="Face Recognition", cursor="hand2", command=self.start_face_recognition,
#                       font=("times new roman", 18, "bold"), bg="darkgreen", fg="WHITE")
#         b1_1.place(x=400, y=620, width=200, height=40)

#     def start_face_recognition(self):
#         thread = threading.Thread(target=self.face_recognition)
#         thread.daemon = True
#         thread.start()

#     def face_recognition(self):
#         def draw_boundary(img, classifier, scaleFactor, minNeighbour, clf):
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbour)
            
#             conn = mysql.connector.connect(host="localhost", username="root", password="@Bhatia98@", database="face_recognizer")
#             my_cursor = conn.cursor()
            
#             for (x, y, w, h) in features:
#                 id, predict = clf.predict(gray_image[y:y+h, x:x+w])
#                 confidence = int((100 * (1 - predict / 300)))
                
#                 my_cursor.execute(f"SELECT Name, StudentId, Section, `Group`, Email FROM student WHERE StudentId={id}")
#                 result = my_cursor.fetchone()
#                 if result:
#                     n, s, i, j, k = map(str, result)
#                 else:
#                     n, s, i, j, k = "Unknown", "Unknown", "Unknown", "N/A", "N/A"
                
#                 color = (0, 255, 0) if confidence > 77 else (0, 0, 255)
#                 cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                
#                 if confidence > 77:
#                     cv2.putText(img, f"ID: {s}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
#                     cv2.putText(img, f"Name: {n}", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
#                     cv2.putText(img, f"Section: {i}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
#                     cv2.putText(img, f"Group: {j}", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
#                     cv2.putText(img, f"Email: {k}", (x, y + 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
#                 else:
#                     cv2.putText(img, "Unknown Face", (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

#         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read("classifier.xml")
        
#         video_cap = cv2.VideoCapture(0)
#         while True:
#             ret, img = video_cap.read()
#             if not ret:
#                 break
#             draw_boundary(img, faceCascade, 1.1, 10, clf)
#             cv2.imshow("Face Recognition", img)
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
#         video_cap.release()
#         cv2.destroyAllWindows()

# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()
