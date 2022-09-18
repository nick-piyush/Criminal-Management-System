from cProfile import label
from cgitb import text
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from login2 import Login2

from tkinter import messagebox
from logging import root
import cv2
import os
from face_recog import*

# from Search import Search as Sr



class Face_recog_main:
    def __init__(self,root):

        Login2 

        self.root=root  
        self.root.geometry('1560x800+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM') 

        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('time new roman',20,'bold'),bg='black',fg='yellow')
        lbl_title.place(x=0,y=0,width=1560,height=40)


        Main_frame=Frame(self.root,relief=RIDGE,bg='gray')
        Main_frame.place(x=0,y=40,width=1560,height=1000)

        img_frame=Frame(Main_frame,relief=RIDGE)
        img_frame.place(x=0,y=0,width=1560,height=300)


        # image 1
        img1=Image.open("images/face_4.jpg")
        img1=img1.resize((780,300),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        bg1=Label(img_frame,image=self.photoimg1)
        bg1.place(x=0,y=0,width=780,height=295)

        # image 2
        img2=Image.open("images/face_5.jpg")
        img2=img2.resize((780,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        bg2=Label(img_frame,image=self.photoimg2)
        bg2.place(x=780,y=0,width=780,height=295)



        #  Down frame------------------------------------------------------>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        bottom_frame=Frame(Main_frame,relief=RIDGE,bg='gray')
        bottom_frame.place(x=0,y=290,width=1560,height=480)

        text_frame=Label(bottom_frame,relief=RIDGE,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('times new roman',26,'bold'),bg='black',fg='yellow')
        text_frame.place(x=0,y=0,width=1550,height=80)

        img4=Image.open("images/face_9.jpg")
        img4=img4.resize((1100,900),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg4=Label(bottom_frame,image=self.photoimg4)
        bg4.place(x=0,y=80,width=1100,height=400)

        # Features
        ftr_frame=Frame(bottom_frame,relief=RIDGE,bg='white')
        ftr_frame.place(x=1100,y=80,width=450,height=400)

        img3=Image.open("images/face_12.jpg")
        img3=img3.resize((550,400),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg3=Label(ftr_frame,image=self.photoimg3)
        bg3.place(x=0,y=0,width=450,height=400)

        L1=Label(ftr_frame,text=' >> Add Data of Criminals',font=('arial',14,'bold'),bg='yellow')
        L1.grid(row=0,column=0,padx=15,pady=10,sticky=W)

        L2=Label(ftr_frame,text=' >> Update Data of Criminals',font=('arial',14,'bold'),bg='yellow')
        L2.grid(row=1,column=0,padx=15,pady=10,sticky=W)

        L3=Label(ftr_frame,text=' >> Delete Data of Criminals',font=('arial',14,'bold'),bg='yellow')
        L3.grid(row=2,column=0,padx=15,pady=10,sticky=W)

        L4=Label(ftr_frame,text=' >> Search Data of Criminals',font=('arial',14,'bold'),bg='yellow')
        L4.grid(row=3,column=0,padx=15,pady=10,sticky=W)

        L5=Label(ftr_frame,text=' >> Face recognition of Criminals',font=('arial',14,'bold'),bg='yellow')
        L5.grid(row=4,column=0,padx=15,pady=10,sticky=W)


        #  Buttons

        button_frame=Frame(bottom_frame,relief=RIDGE,bg='lightgray')
        button_frame.place(x=140,y=100,width=775,height=160)


        # add button 
        btn_add=Button(button_frame,text='Data Page',command=datapage,font=('arial',14,'bold'),width=14,height=6,bg='green',fg='white')
        btn_add.grid(row=0,column=0,padx=8,pady=5)

        # search
        btn_search=Button(button_frame,text='Search',command=search,font=('arial',14,'bold'),width=14,height=6,bg='brown',fg='white')
        btn_search.grid(row=0,column=1,padx=8,pady=5)

        # update button
        # btn_update=Button(button_frame,text='Train Face',command=self.train_classifiers,font=('arial',14,'bold'),width=14,height=6,bg='Orange',fg='white')
        # btn_update.grid(row=0,column=2,padx=8,pady=5)

        # delete button
        btn_delete=Button(button_frame,text='Face Recognise',command=self.face_recognition,font=('arial',14,'bold'),width=14,height=6,bg='red',fg='white')
        btn_delete.grid(row=0,column=2,padx=8,pady=5)

        # clear button
        btn_clear=Button(button_frame,text='All Records',command=alldata,font=('arial',14,'bold'),width=14,height=6,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=8,pady=5)



        # btn1=Button(img_frame,image=self.photoimg1)
        # btn1.place(x=0,y=0,width=220,height=220)
        
  
    

    ## train data function

    def train_classifiers(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #grayscale img
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("TRAINING",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

    ####train the classifier#######

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifiers.xml")
        # cv2.destroyAllwindows()
        messagebox.showinfo("Result","Training datasets completed!!")



    ## face recognition

    def face_recognition(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
                
            coord=[]
                
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                
        
                if confidence>80:
                    cv2.putText(img,f"Criminal_suspect",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,255),3)
                    


                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
                    cv2.putText(img,"Unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                        
                        
                coord=[x,y,w,h]
                    
            return  coord   
            
        def recognize(img,clf,facecascade):
            coord=draw_boundary(img,facecascade,1.1,10,(255,25,255),"Face",clf)
                    
            return img
            
        facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifiers.xml")
            
        video_cap=cv2.VideoCapture(0)
            
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,facecascade)
            cv2.imshow("welcome to face recognize",img)
                
            if cv2.waitKey(1)==13:
                break
        video_cap.release()




def datapage():
    os.system('Criminal.py')


def search():
    os.system('Search.py')


# def datapage():
#     os.system('Criminal.py')


def alldata():
    os.system('Display.py')
                




if __name__=="__main__":
    root=Tk()
    obj=Face_recog_main(root)
    root.mainloop()   