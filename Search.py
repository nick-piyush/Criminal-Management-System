from tkinter import*
from tkinter import ttk
from tkinter.font import BOLD
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
from Criminal import *



class Search:

    def __init__(self, root):

        self.root=root  
        self.root.geometry('1560x800+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM/DisplayData')

        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('time new roman',20,'bold'),bg='black',fg='yellow')
        lbl_title.place(x=0,y=0,width=1560,height=40)

        Main_frame=Frame(self.root,relief=RIDGE,bg='lightblue')
        Main_frame.place(x=0,y=40,width=1560,height=780)


        # search_frame=LabelFrame(Main_frame,relief=RIDGE,text='Search Records',font=('times new roman',15,'bold'),fg='red',bg='white')
        # search_frame.place(x=10,y=10,width=1520,height=730)
        
        search_frame=LabelFrame(Main_frame,relief=RIDGE,text='Search Criminal Record',font=('sans-serif',17,'bold'),fg='red',bg="lightblue")
        search_frame.place(x=0,y=0,width=1560,height=780)


        search_by=Label(search_frame,text='Search By:',font=('arial',13,'bold'),bg="red",fg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=8,pady=12)

        self.var_com_search=StringVar()

        combo_search_box=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',15,'bold'),width=18,state='readonly')
        combo_search_box['value']=('Select Option','Case_id','Criminal_no','Criminal_name')
        combo_search_box.current(1)
        combo_search_box.grid(row=1,column=0,sticky=W,padx=8,pady=5)

        self.var_search=StringVar()


        search_txt=ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=('arial',15,'bold'))
        search_txt.grid(row=1,column=1,sticky=W,padx=5,pady=5)

        

        # search button
        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',15,'bold'),width=15,bg='blue',fg='white')
        btn_search.grid(row=1,column=3,sticky=W,padx=5,pady=5)

        # # all button
        # btn_all=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',13,'bold'),width=14,bg='blue',fg='white')
        # btn_all.grid(row=2,column=0,sticky=W,padx=5,pady=5)


        # Face Recognition Button


        button_frame2=Frame(search_frame,relief=RIDGE,bg='lightblue')
        button_frame2.place(x=1100,y=55,width=255,height=300)

        img_fid=Image.open('images/face_3.jpg')
        img_fid=img_fid.resize((280,300),Image.LANCZOS)
        self.bg1=ImageTk.PhotoImage(img_fid)
        self.bg_image1=Label(button_frame2,image=self.bg1).place(x=0,y=0,relwidth=1,relheight=1)

        # btn_face2=Button(search_frame,text='Face recognise',font=('arial',14,'bold'),width=14,height=7,bg='darkblue',fg='white')
        # btn_face2.grid(row=3,column=0,padx=10,pady=65)



        # table frame
        table_frame1=Frame(search_frame,relief=RIDGE)
        table_frame1.place(x=5,y=450,width=1520,height=250)

        
        # scroll bar 
        scroll_x=ttk.Scrollbar(table_frame1,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame1,orient=VERTICAL)

        self.criminal_table2=ttk.Treeview(table_frame1,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Sans-serif',13,BOLD))


        style = ttk.Style()
        style.configure("Treeview.Column", font=('Sans-serif',13,BOLD))
        

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

        self.criminal_table2.column('1',anchor=CENTER,width=80)
        self.criminal_table2.column('3',anchor=CENTER,width=120)
        self.criminal_table2.column('4',anchor=CENTER,width=100)
        self.criminal_table2.column('2',anchor=CENTER,width=100)
        self.criminal_table2.column('5',anchor=CENTER,width=100)
        self.criminal_table2.column('6',anchor=CENTER,width=100)
        self.criminal_table2.column('7',anchor=CENTER,width=120)
        self.criminal_table2.column('8',anchor=CENTER,width=100)
        self.criminal_table2.column('9',anchor=CENTER,width=100)
        self.criminal_table2.column('10',anchor=CENTER,width=100)
        self.criminal_table2.column('11',anchor=CENTER,width=100)
        self.criminal_table2.column('12',anchor=CENTER,width=130)
        self.criminal_table2.column('13',anchor=CENTER,width=70)
        self.criminal_table2.column('14',anchor=CENTER,width=70)
    
        
        self.criminal_table2.pack(fill=BOTH,expand=1)


        self.criminal_table2.bind("<ButtonRelease>",Criminal.get_cursor)






    # fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Atish@sql',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from management.criminal')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.criminal_table2.delete(*self.criminal_table2.get_children())
            for i in data:
                self.criminal_table2.insert('',END,values=i)
            conn.commit()
        conn.close()




    
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




if __name__=="__main__":
        root=Tk()
        obj=Search(root)
        root.mainloop() 