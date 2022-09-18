from tkinter import*
from tkinter import ttk
from tkinter import font
import mysql.connector
from Criminal import *



class Display:

    def __init__(self, root):
        
        self.root=root  
        self.root.geometry('1560x800+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM/DisplayData')

        lbl_title=Label(self.root,text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('time new roman',20,'bold'),bg='black',fg='yellow')
        lbl_title.place(x=0,y=0,width=1560,height=40)

        Main_frame=Frame(self.root,relief=RIDGE,bg='gray')
        Main_frame.place(x=0,y=40,width=1560,height=1000)


        down_frame=LabelFrame(Main_frame,relief=RIDGE,text='Criminal Records',font=('times new roman',15,'bold'),fg='red',bg='white')
        down_frame.place(x=10,y=10,width=1520,height=730)


        # table frame
        table_frame=Frame(down_frame,relief=RIDGE)
        table_frame.place(x=5,y=10,width=1510,height=690)

        
        
        # scroll bar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.criminal_table=ttk.Treeview(table_frame,column=("1","2","3","4","5","6","7","8","9","10","11","12","13","14"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Sans-serif',13,font.BOLD))


        style = ttk.Style()
        style.configure("Treeview.Column", font=('Sans-serif',13,font.BOLD))
        

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

        self.criminal_table.column('1',anchor=CENTER,width=80)
        self.criminal_table.column('3',anchor=CENTER,width=120)
        self.criminal_table.column('4',anchor=CENTER,width=100)
        self.criminal_table.column('2',anchor=CENTER,width=100)
        self.criminal_table.column('5',anchor=CENTER,width=100)
        self.criminal_table.column('6',anchor=CENTER,width=100)
        self.criminal_table.column('7',anchor=CENTER,width=120)
        self.criminal_table.column('8',anchor=CENTER,width=100)
        self.criminal_table.column('9',anchor=CENTER,width=100)
        self.criminal_table.column('10',anchor=CENTER,width=100)
        self.criminal_table.column('11',anchor=CENTER,width=100)
        self.criminal_table.column('12',anchor=CENTER,width=130)
        self.criminal_table.column('13',anchor=CENTER,width=70)
        self.criminal_table.column('14',anchor=CENTER,width=70)
    
        
        self.criminal_table.pack(fill=BOTH,expand=1)


        self.criminal_table.bind("<ButtonRelease>",Criminal.get_cursor)
        self.fetch_data()




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



if __name__=="__main__":
        root=Tk()
        obj=Display(root)
        root.mainloop()  