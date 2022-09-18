from tkinter import*
from tkinter import ttk
from turtle import bgcolor
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from fileinput import filename
from logging import root
from re import T
import cv2
from cv2 import imshow
# from google.colab.patches import cv2_imshow
import os
from face_recog import*

# from login2 import Login2


class Criminal:

    def __init__(self, root):
        # Login2 
        self.root=root  
        self.root.geometry('1560x800+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM') 

        # variables
        self.var_case_id = StringVar()
        self.var_criminal_no = StringVar()
        self.var_name = StringVar()
        self.var_nickname = StringVar()
        self.var_arrest_date = StringVar()
        self.var_date_of_crime = StringVar()
        self.var_address = StringVar()
        self.var_age = StringVar()
        self.var_occupation = StringVar()
        self.var_birthMark = StringVar()
        self.var_crime_type = StringVar()
        self.var_father_name = StringVar()
        self.var_gender = StringVar()
        self.var_wanted = StringVar()
        



        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('time new roman',20,'bold'),bg='black',fg='yellow')
        lbl_title.place(x=0,y=0,width=1560,height=40)


        # # firstlogo image
        # img_logo=Image.open('images/firstlogo.jpg')
        # img_logo=img_logo.resize((30,30),Image.ANTIALIAS)
        # self.photo_logo=ImageTk.PhotoImage(img_logo)

        # self.logo=Label(self.root,image=self.photo_logo)
        # self.logo.place(x=150,y=5,width=30,height=30)

        

        #Main frame
        Main_frame=Frame(self.root,relief=RIDGE,bg='gray')
        Main_frame.place(x=0,y=40,width=1560,height=1000)

        # upper frame
        upper_frame=LabelFrame(Main_frame,relief=RIDGE, text='Criminal Information',font=('sans-serif',17,'bold'),fg='red',bg='lightgreen')
        upper_frame.place(x=10,y=10,width=780,height=480)
    
        # Labels Entery

        #  Case Id 
        caseid=Label(upper_frame,text='Case ID:',font=('arial',13,'bold'),bg='lightgreen')
        caseid.grid(row=0,column=0,padx=3,sticky=W)

        caseentry=ttk.Entry(upper_frame,textvariable=self.var_case_id,width=25,font=('arial',13,'bold'))
        caseentry.grid(row=0,column=1,padx=3,sticky=W)

        # Criminal No
        lbl_criminal_no=Label(upper_frame,text='Criminal No.:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_criminal_no.grid(row=0,column=2,sticky=W,padx=3,pady=7)

        txt_criminal_no=ttk.Entry(upper_frame,textvariable=self.var_criminal_no,width=25,font=('arial',13,'bold'))
        txt_criminal_no.grid(row=0,column=3,padx=3,pady=7)

        # Criminal Name
        lbl_Name=Label(upper_frame,text='Criminal Name:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_Name.grid(row=1,column=0,sticky=W,padx=3,pady=7)

        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=25,font=('arial',13,'bold'))
        txt_Name.grid(row=1,column=1,sticky=W,padx=3,pady=7)


        # NickName
        lbl_nickname=Label(upper_frame,text='Nickname:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_nickname.grid(row=1,column=2,sticky=W,padx=3,pady=7)

        txt_nickname=ttk.Entry(upper_frame,textvariable=self.var_nickname,width=25,font=('arial',13,'bold'))
        txt_nickname.grid(row=1,column=3,padx=3,pady=7)



        # Arrest Date
        lbl_arrestDate=Label(upper_frame,text='Arrest Date:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_arrestDate.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_arrestDate=ttk.Entry(upper_frame,textvariable=self.var_arrest_date,width=25,font=('arial',13,'bold'))
        txt_arrestDate.grid(row=2,column=1,padx=2,pady=7)


        #  Date Of Crime
        lbl_dateofcrime=Label(upper_frame,text='Date of Crime:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_dateofcrime.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        txt_dateofcrime=ttk.Entry(upper_frame,textvariable=self.var_date_of_crime,width=25,font=('arial',13,'bold'))
        txt_dateofcrime.grid(row=2,column=3,sticky=W,padx=2,pady=7)



        #  Address
        lbl_address=Label(upper_frame,text='Address:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_address.grid(row=3,column=0,sticky=W,padx=3,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=25,font=('arial',13,'bold'))
        txt_address.grid(row=3,column=1,padx=3,pady=7)


        #Age 
        lbl_age=Label(upper_frame,text='Age:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_age.grid(row=3,column=2,sticky=W,padx=3,pady=7)

        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=25,font=('arial',13,'bold'))
        txt_age.grid(row=3,column=3,padx=3,pady=7)

    
        #  occupution
        lbl_occupution=Label(upper_frame,text='Occupution:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_occupution.grid(row=4,column=0,sticky=W,padx=3,pady=7)

        txt_occupution=ttk.Entry(upper_frame,textvariable=self.var_occupation,width=25,font=('arial',13,'bold'))
        txt_occupution.grid(row=4,column=1,padx=3,pady=7)


        # birthMark
        lbl_birthMark=Label(upper_frame,text='Birth Mark:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_birthMark.grid(row=4,column=2,sticky=W,padx=3,pady=7)

        txt_birthMark=ttk.Entry(upper_frame,textvariable=self.var_birthMark,width=25,font=('arial',13,'bold'))
        txt_birthMark.grid(row=4,column=3,sticky=W,padx=3,pady=7)


        # Crime Type
        lbl_crimeType=Label(upper_frame,text='Crime Type:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_crimeType.grid(row=5,column=0,sticky=W,padx=3,pady=7)

        txt_crimeType=ttk.Entry(upper_frame,textvariable=self.var_crime_type,width=25,font=('arial',13,'bold'))
        txt_crimeType.grid(row=5,column=1,padx=3,pady=7)


        # Father Name
        lbl_fatherName=Label(upper_frame,text='Father Name:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_fatherName.grid(row=5,column=2,sticky=W,padx=3,pady=7)

        txt_fatherName=ttk.Entry(upper_frame,textvariable=self.var_father_name,width=25,font=('arial',13,'bold'))
        txt_fatherName.grid(row=5,column=3,padx=3,pady=7)


        # gender
        lbl_gender=Label(upper_frame,text='Gender:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_gender.grid(row=7,column=0,sticky=W,padx=3, pady=7)
        

        # Wanted 
        lbl_wanted=Label(upper_frame,text='Wanted:',font=('arial',13,'bold'),bg='lightgreen')
        lbl_wanted.grid(row=7,column=2,sticky=W,padx=3,pady=7)

        #  Radio Button Gender
        radio_frame_gender=Frame(upper_frame,relief=RIDGE,bg='lightgreen')
        radio_frame_gender.place(x=130,y=235,width=190,height=30)

    
        male=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Male',value='Male',font=('arial',12,'bold'),bg='white')
        male.grid(row=0,column=0,pady=2,padx=5,sticky=W)

        female=Radiobutton(radio_frame_gender,variable=self.var_gender,text='Female',value='Female',font=('arial',12,'bold'),bg='white')
        female.grid(row=0,column=1,pady=2,padx=5,sticky=W)

    
        #  Radio Button Wanted
        radio_frame_wanted=Frame(upper_frame,relief=RIDGE,bg='lightgreen')
        radio_frame_wanted.place(x=490,y=235,width=190,height=30)


        yes=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='Yes',value='yes',font=('arial',12,'bold'),bg='white')
        yes.grid(row=0,column=0,pady=2,padx=5,sticky=W)

        no=Radiobutton(radio_frame_wanted,variable=self.var_wanted,text='No',value='no',font=('arial',12,'bold'),bg='white')
        no.grid(row=0,column=1,pady=2,padx=5,sticky=W)



        # Take photo sample 

        btn_takephoto=Button(upper_frame,command=self.generate_dataset,text='Take Photo',font=('arial',13,'bold'),width=14,height=3,bg='darkblue',fg='white')
        btn_takephoto.grid(row=8,column=1,sticky=W,padx=3,pady=7)
        

        # Train data button

        btn_face=Button(upper_frame,command=self.train_classifiers,text='Train Data',font=('arial',13,'bold'),width=14,height=3,bg='orange',fg='white')
        btn_face.grid(row=8,column=3,sticky=W,padx=3, pady=7)


        # Button
        button_frame=Frame(upper_frame,relief=RIDGE,bg='lightgreen')
        button_frame.place(x=10,y=400,width=750,height=45)


        # add button 
        btn_add=Button(button_frame,command=self.add_data,text='Save Record',font=('arial',13,'bold'),width=14,bg='green',fg='white')
        btn_add.grid(row=0,column=0,padx=3,pady=5)

        # update button
        btn_update=Button(button_frame,command=self.update_data,text='Update',font=('arial',13,'bold'),width=14,bg='green',fg='white')
        btn_update.grid(row=0,column=1,padx=3,pady=5)

        # delete button
        btn_delete=Button(button_frame,command=self.delete_data,text='Delete',font=('arial',13,'bold'),width=14,bg='red',fg='white')
        btn_delete.grid(row=0,column=2,padx=3,pady=5)

        # clear button
        btn_clear=Button(button_frame,command=self.clear_data,text='Clear',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=0,column=3,padx=3,pady=5)



        # Search Frame----------------------------------------------------------------------------------->>>>>

        search_frame=LabelFrame(Main_frame,relief=RIDGE,text='Search Criminal Record',font=('times new roman',15,'bold'),fg='red',bg="lightblue")
        search_frame.place(x=800,y=10,width=730,height=480)


        search_by=Label(search_frame,text='Search By:',font=('arial',12,'bold'),bg="red",fg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        self.var_com_search=StringVar()

        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',12,'bold'),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no','Criminal_name')
        combo_search_box.current(1)
        combo_search_box.grid(row=1,column=0,sticky=W,padx=5,pady=5)

        self.var_search=StringVar()


        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=('arial',12,'bold'))
        search_txt.grid(row=1,column=1,sticky=W,padx=5,pady=5)

        

        # search button
        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=1,column=3,sticky=W,padx=5,pady=5)

        # all button
        btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        btn_all.grid(row=2,column=0,sticky=W,padx=5,pady=5)


        # Face Recognition Button


        button_frame2=Frame(search_frame,relief=RIDGE,bg='lightblue')
        button_frame2.place(x=500,y=110,width=155,height=200)

        img_fid=Image.open('images/face_3.jpg')
        img_fid=img_fid.resize((180,200),Image.LANCZOS)
        self.bg1=ImageTk.PhotoImage(img_fid)
        self.bg_image1=Label(button_frame2,image=self.bg1).place(x=0,y=0,relwidth=1,relheight=1)

        btn_face2=Button(button_frame2,command=self.face_recognition,text='Face recognise',font=('arial',13,'bold'),width=14,bg='darkblue',fg='white')
        btn_face2.grid(row=4,column=3,padx=2,pady=165)



        # table frame
        table_frame1=Frame(search_frame,relief=RIDGE)
        table_frame1.place(x=2,y=350,width=720,height=100)

        
        # scroll bar 
        scroll_x=ttk.Scrollbar(table_frame1,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame1,orient=VERTICAL)

        self.criminal_table2=ttk.Treeview(table_frame1,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table2.xview)
        scroll_y.config(command=self.criminal_table2.yview)


        self.criminal_table2.heading('1',text='CaseID')
        self.criminal_table2.heading('2',text='Crime_No')
        self.criminal_table2.heading('3',text='Criminal Name')
        self.criminal_table2.heading('4',text='NickName')
        self.criminal_table2.heading('5',text='ArrestDate')
        self.criminal_table2.heading('6',text='DateOfCrime')
        self.criminal_table2.heading('7',text='Address')
        self.criminal_table2.heading('8',text='Age')
        self.criminal_table2.heading('9',text='Occupation')
        self.criminal_table2.heading('10',text='Birth Mark')
        self.criminal_table2.heading('11',text='Crime Type')
        self.criminal_table2.heading('12',text='Father Name')
        self.criminal_table2.heading('13',text='Gender')
        self.criminal_table2.heading('14',text='Wanted')


        self.criminal_table2['show']='headings'

        self.criminal_table2.column('1',width=50)
        self.criminal_table2.column('2',width=60)
        self.criminal_table2.column('3',width=90)
        self.criminal_table2.column('4',width=50)
        self.criminal_table2.column('5',width=80)
        self.criminal_table2.column('6',width=80)
        self.criminal_table2.column('7',width=100)
        self.criminal_table2.column('8',width=40)
        self.criminal_table2.column('9',width=80)
        self.criminal_table2.column('10',width=40)
        self.criminal_table2.column('11',width=80)
        self.criminal_table2.column('12',width=100)
        self.criminal_table2.column('13',width=50)
        self.criminal_table2.column('14',width=50)
    
        
        self.criminal_table2.pack(fill=BOTH,expand=1)


        self.criminal_table2.bind("<ButtonRelease>",self.get_cursor)




        # Down frame------------------------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


        down_frame=LabelFrame(Main_frame,relief=RIDGE,text='Criminal Records',font=('times new roman',15,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=500,width=1520,height=245)


        # table frame
        table_frame=Frame(down_frame,relief=RIDGE)
        table_frame.place(x=5,y=10,width=1510,height=208)

        
        
        # scroll bar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.criminal_table.xview)
        scroll_y.config(command=self.criminal_table.yview)


        self.criminal_table.heading('1',text='CaseID')
        self.criminal_table.heading('2',text='Crime_No')
        self.criminal_table.heading('3',text='Criminal Name')
        self.criminal_table.heading('4',text='NickName')
        self.criminal_table.heading('5',text='ArrestDate')
        self.criminal_table.heading('6',text='DateOfCrime')
        self.criminal_table.heading('7',text='Address')
        self.criminal_table.heading('8',text='Age')
        self.criminal_table.heading('9',text='Occupation')
        self.criminal_table.heading('10',text='Birth Mark')
        self.criminal_table.heading('11',text='Crime Type')
        self.criminal_table.heading('12',text='Father Name')
        self.criminal_table.heading('13',text='Gender')
        self.criminal_table.heading('14',text='Wanted')


        self.criminal_table['show']='headings'

        self.criminal_table.column('1',width=80)
        self.criminal_table.column('2',width=100)
        self.criminal_table.column('3',width=120)
        self.criminal_table.column('4',width=100)
        self.criminal_table.column('5',width=100)
        self.criminal_table.column('6',width=100)
        self.criminal_table.column('7',width=120)
        self.criminal_table.column('8',width=100)
        self.criminal_table.column('9',width=100)
        self.criminal_table.column('10',width=100)
        self.criminal_table.column('11',width=100)
        self.criminal_table.column('12',width=130)
        self.criminal_table.column('13',width=70)
        self.criminal_table.column('14',width=70)
    
        
        self.criminal_table.pack(fill=BOTH,expand=1)


        self.criminal_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()




    #   Add function

    def add_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are required', parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root', password='Atish@sql',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into criminal (Case_id,Criminal_no,Criminal_name,Nick_name,arrest_date,dateOfcrime,address,age,occupation,BirthMark,crimeType,fatherName,gender,wanted) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                    self.var_case_id.get(),
                                                    self.var_criminal_no.get(),
                                                    self.var_name.get(),
                                                    self.var_nickname.get(),
                                                    self.var_arrest_date.get(),
                                                    self.var_date_of_crime.get(),
                                                    self.var_address.get(),
                                                    self.var_age.get(),
                                                    self.var_occupation.get(),
                                                    self.var_birthMark.get(),
                                                    self.var_crime_type.get(),
                                                    self.var_father_name.get(),
                                                    self.var_gender.get(),
                                                    self.var_wanted.get()

                                                )) 

                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been added')
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')



    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Atish@sql',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from management.criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table.delete(*self.criminal_table.get_children())
            for i in data:
                self.criminal_table.insert('',END,values=i)
            conn.commit()
        conn.close()



    # get cursor

    def get_cursor(self,event=""):
        cursor_row=self.criminal_table2.focus()
        content=self.criminal_table2.item(cursor_row)
        data=content['values']

        self.var_case_id.set(data[0])
        self.var_criminal_no.set(data[1])
        self.var_name.set(data[2])
        self.var_nickname.set(data[3])
        self.var_arrest_date.set(data[4])
        self.var_date_of_crime.set(data[5])
        self.var_address.set(data[6])
        self.var_age.set(data[7])
        self.var_occupation.set(data[8])
        self.var_birthMark.set(data[9])
        self.var_crime_type.set(data[10])
        self.var_father_name.set(data[11])
        self.var_gender.set(data[12])
        self.var_wanted.set(data[13])



    # update data
    def update_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('update','Are you sure to update this criminal record')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Atish@sql',database='management')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update criminal set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(

                        
                        self.var_criminal_no.get(),
                        self.var_name.get(),
                        self.var_nickname.get(),
                        self.var_arrest_date.get(),
                        self.var_date_of_crime.get(),
                        self.var_address.get(),
                        self.var_age.get(),
                        self.var_occupation.get(),
                        self.var_birthMark.get(),
                        self.var_crime_type.get(),
                        self.var_father_name.get(),
                        self.var_gender.get(),
                        self.var_wanted.get(),
                        self.var_case_id.get()
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been successfully updated')
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')


    # Delete function
    def delete_data(self):
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                delete=messagebox.askyesno('delete','Are you sure to delete this criminal record')
                if delete>0:

                    conn=mysql.connector.connect(host='localhost',username='root',password='Atish@sql',database='management')
                    my_cursor=conn.cursor()
                    sql='delete from criminal where Case_id=%s'
                    value=(self.var_case_id.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                self.clear_data()
                conn.close()
                messagebox.showinfo('Success','Criminal record has been successfully deleted')
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')



    # clear data
    def clear_data(self):
        self.var_case_id.set("")
        self.var_criminal_no.set("")
        self.var_name.set("")
        self.var_nickname.set("")
        self.var_arrest_date.set("")
        self.var_date_of_crime.set("")
        self.var_address.set("")
        self.var_age.set("")
        self.var_occupation.set("")
        self.var_birthMark.set("")
        self.var_crime_type.set("")
        self.var_father_name.set("")
        self.var_gender.set("")
        self.var_wanted.set("")
        


    # Search Data
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Atish@sql',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from criminal where ' +str(self.var_com_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.criminal_table2.delete(*self.criminal_table2.get_children())
                    for i in rows:
                        self.criminal_table2.insert('',END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due to{str(es)}')
                



    #======== generate data set and take a sample==== 
    def generate_dataset(self): 
        if self.var_case_id.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Atish@sql',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from criminal")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+1
                my_cursor.execute('update criminal set Criminal_no=%s,Criminal_name=%s,Nick_name=%s,arrest_date=%s,dateOfcrime=%s,address=%s,age=%s,occupation=%s,BirthMark=%s,crimeType=%s,fatherName=%s,gender=%s,wanted=%s where Case_id=%s',(

                            
                            self.var_criminal_no.get(),
                            self.var_name.get(),
                            self.var_nickname.get(),
                            self.var_arrest_date.get(),
                            self.var_date_of_crime.get(),
                            self.var_address.get(),
                            self.var_age.get(),
                            self.var_occupation.get(),
                            self.var_birthMark.get(),
                            self.var_crime_type.get(),
                            self.var_father_name.get(),
                            self.var_gender.get(),
                            self.var_wanted.get(),
                            self.var_case_id.get()==id+1
                        ))
                conn.commit() 
                self.fetch_data()  
                # self.reset_data()
                conn.close()


            #    ====== load pred edifine ======
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scling factor 1.3
                    #minium neighbour 5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450),interpolation=cv2.INTER_AREA)
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)  
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face) 
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()            
                cv2.destroyAllWindows()
            
                messagebox.showinfo("Result","generating data sets compled!!")
            except Exception as es:
                messagebox.showerror("error",f"due to : {str(es)}",parent=self.root)
  
    



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
        cv2.destroyAllWindows()
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
                    cv2.putText(img,"unknown face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)
                        
                        
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



                          
if __name__=="__main__":
    root=Tk()
    obj=Criminal(root)
    root.mainloop()   