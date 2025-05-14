import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


# Base directory for images
base_dir = r"images"
class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face_Recognition_System")


        # Title label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = os.path.join(base_dir, "train2.jpg")
        img_top = Image.open(img_top)
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)  # Resize to fit the frame
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)
        
        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman", 30, "bold"), bg="RED", fg="WHITE")
        b1_1.place(x=0,y=380,width=1530,height=60)

        img_bottom = os.path.join(base_dir, "multipeople.jpg")
        img_bottom = Image.open(img_bottom)
        img_bottom = img_bottom.resize((1530, 325), Image.Resampling.LANCZOS)  # Resize to fit the frame
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] 

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")  #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])



            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        #Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed..")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()




# import os 
# import cv2
# import numpy as np
# import dlib
# from mtcnn import MTCNN
# from PIL import Image
# from tkinter import *
# from tkinter import messagebox

# # Base directory for images
# data_dir = "data"
# classifier_file = "classifier.xml"

# class Train:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("800x500")
#         self.root.title("Train Face Recognition Model")
        
#         title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Arial", 20, "bold"), bg="white", fg="red")
#         title_lbl.pack(pady=10)
        
#         train_btn = Button(self.root, text="TRAIN DATA", command=self.train_classifier, font=("Arial", 15, "bold"), bg="green", fg="white")
#         train_btn.pack(pady=20)

#     def train_classifier(self):
#         detector = MTCNN()
#         face_recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
#         shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#         faces = []
#         ids = []
        
#         for file in os.listdir(data_dir):
#             img_path = os.path.join(data_dir, file)
#             img = cv2.imread(img_path)
#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
#             detections = detector.detect_faces(img)
#             for detection in detections:
#                 x, y, w, h = detection['box']
#                 face = gray[y:y+h, x:x+w]
#                 face = cv2.resize(face, (150, 150))
#                 id = int(file.split('.')[1])
                
#                 faces.append(face)
#                 ids.append(id)
#                 cv2.imshow("Training", face)
#                 cv2.waitKey(1)
        
#         ids = np.array(ids)
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.train(faces, ids)
#         clf.write(classifier_file)
#         cv2.destroyAllWindows()
#         messagebox.showinfo("Result", "Training Completed Successfully")

# if __name__ == "__main__":
#     root = Tk()
#     obj = Train(root)
#     root.mainloop()