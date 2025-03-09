from tkinter import *
import time
import ttkthemes
# import ttkthemes.themed_tk
from tkinter import ttk,messagebox
import pymysql




#Function Part
#Date and time 
def clock():
    date = time.strftime('%d/%m/%Y')
    currentime = time.strftime('%H:%M:%S')
    datetime_Label.config(text=f'   Date:{date} \n Time : {currentime}')
    datetime_Label.after(1000,clock )

#Text slider 
count=0
text = '' 
def slidertext():
    global text,count
    if count == len(s):
        count = 0
        text = ''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slidertext)


#Connect to database button working
def connect_database():
    def connect():
        global mycursor , DB_con
        try:
            DB_con = pymysql.connect(host=hostEntry.get(),user=userEntry.get(),password=passwordEntry.get())                  #These pymysql with connect python with mysql and fetch data using that get function
            mycursor =DB_con.cursor()   #helps to executing the commands i.e updating,connecting,delete
            messagebox.showinfo('Success', 'Connected to Database', parent=connectwindow)
        except:
            messagebox.showerror('ERROR', 'Invalid Details', parent=connectwindow)

        #MYSQL COMMANDS TO RUNS THE QUERIES FROM PYTHON BY USING MYCURSOR    
        try:
        
            Query='create database studentmanagementsystem'
            mycursor.execute(Query)
            Query='use studentmanagementsystem'
            mycursor.execute(Query)
            Query='create table student(name varchar(30),id int not null primary key, mobile varchar(10),email varchar(30),address varchar(100),gender varchar(20),dob varchar(20),admission_year varchar(10), passing_year year)'
            mycursor.execute(Query)
        
        except:
            Query='use studentmanagementsystem'
            mycursor.execute(Query)  
        addstudentButton.config(state='normal')
        searchstudentButton.config(state='normal')
        updatestudentButton.config(state='normal')
        showstudentButton.config(state='normal')
        exportdataButton.config(state='normal')
        delstudentButton.config(state='normal')
        connectwindow.destroy()

        


#creating the window after clicking connect to database
    connectwindow=Toplevel()    #used to create a window on top of all other windows 
    connectwindow.grab_set()    #its use to not minimize a particular window if clicked outside the window
    connectwindow.geometry('470x250+600+230')
    connectwindow.title('Database Connection')
    connectwindow.resizable(0,0)



#Hostname Field
    hostnamelabel=Label(connectwindow,text='Host Name',font=('arial', 15, 'bold'))
    hostnamelabel.grid(row=0,column=0,padx=40)
    #HOSTNAME ENTRY
    hostEntry=Entry(connectwindow,font=('arial',15),bd=2)
    hostEntry.grid(row=0,column=1,padx=20,pady=20)
    
#Username Field
    usernamelabel=Label(connectwindow,text='User Name',font=('arial', 15, 'bold'))
    usernamelabel.grid(row=1,column=0,padx=40)
    #USERNAME ENTRY
    userEntry=Entry(connectwindow,font=('arial',15),bd=2)
    userEntry.grid(row=1,column=1,padx=20,pady=20)

#Password Field
    passwordlabel=Label(connectwindow,text='Password',font=('arial', 15, 'bold'))
    passwordlabel.grid(row=2,column=0,padx=40)
    #Password ENTRY
    passwordEntry=Entry(connectwindow,font=('arial',15),bd=2)
    passwordEntry.grid(row=2,column=1,padx=20,pady=20)


#Database Connect Button 
    connectButton=ttk.Button(connectwindow,text='CONNECT',width=20,command=connect)
    connectButton.grid(row=3,columnspan=2)


def add_student():
    def add_data():
        if nameEntry.get()=='' or idEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or DOBEntry.get()=='' or ad_yearEntry.get()=='' or pass_yearEntry.get=='':
            messagebox.showerror('ERROR','All Fields Required', parent=add_window)

        else:
            Query='insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(Query,(nameEntry.get(),idEntry.get(),phoneEntry.get(),emailEntry.get(), addressEntry.get(), genderEntry.get(), DOBEntry.get(),ad_yearEntry.get(),pass_yearEntry.get()))

            DB_con.commit()
            result = messagebox.askyesno('Clear form ??')
            print(result)


    add_window =Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)

    #Name
    namelabel=Label(add_window,text='NAME',font=('times new roman',20,'bold'))
    namelabel.grid(row= 1,column=0,padx=30,pady=15,stick=W)
    nameEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=10,pady=15)

    #ID 
    idlabel=Label(add_window,text='ID',font=('times new roman',20,'bold'))
    idlabel.grid(row= 0,column=0,padx=30,pady=15,stick=W)
    idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,padx=10,pady=15)

    #phone
    phonelabel=Label(add_window,text='Mobile_No',font=('times new roman',20,'bold'))
    phonelabel.grid(row= 2,column=0,padx=30,pady=15,stick=W)
    phoneEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,padx=10,pady=15)

    #Email
    emaillabel=Label(add_window,text='EMAIL',font=('times new roman',20,'bold'))
    emaillabel.grid(row= 3,column=0,padx=30,pady=15,stick=W)
    emailEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,padx=10,pady=15)

    #address
    addresslabel=Label(add_window,text='ADDRESS',font=('times new roman',20,'bold'))
    addresslabel.grid(row= 4,column=0,padx=30,pady=15,stick=W)
    addressEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,padx=10,pady=15)

    #Gender
    genderlabel=Label(add_window,text='GENDER',font=('times new roman',20,'bold'))
    genderlabel.grid(row= 5,column=0,padx=30,pady=15,stick=W)
    genderEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,padx=10,pady=15)

    #DOB
    DOBlabel=Label(add_window,text='Date-Of-Birth',font=('times new roman',20,'bold'))
    DOBlabel.grid(row= 6,column=0,padx=30,pady=15,stick=W)
    DOBEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    DOBEntry.grid(row=6,column=1,padx=10,pady=15)

    #Admission Year
    ad_yearlabel=Label(add_window,text='Admission Year',font=('times new roman',20,'bold'))
    ad_yearlabel.grid(row= 7,column=0,padx=30,pady=15,stick=W)
    ad_yearEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    ad_yearEntry.grid(row=7,column=1,padx=10,pady=15)

    #Passing Year
    pass_yearlabel=Label(add_window,text='Passing Year',font=('times new roman',20,'bold'))
    pass_yearlabel.grid(row= 8,column=0,padx=30,pady=15,stick=W)
    pass_yearEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    pass_yearEntry.grid(row=8,column=1,padx=10,pady=15)


    add_student_Button=ttk.Button(add_window,text='ADD STUDENT',width=30,command=add_data)
    add_student_Button.grid(row=9,columnspan=2,pady=15)





















#GUI Part
root = ttkthemes.ThemedTk()  #themes
root.get_themes()
root.set_theme('radiance')         #themes ()

root.geometry ('1200x800+8+0')

root.title('Student Management System')
root.resizable(False,False)  

#Date and time portion
datetime_Label=Label(root, font=('times new roman',18, 'bold'))
datetime_Label.place(x=5,y=20)
clock()


#Sliding Text
s='Student Management System'
sliderLabel=Label(root,text=s,font=('arial',25, 'italic bold'),width = 40)
sliderLabel.place(x=200,y=25)
slidertext()

#Connect to DataBase button
connectButton =ttk.Button(root,text='Connect DataBase',command=connect_database )
connectButton.place(x=1000,y=30)


#Left Portion
leftFrame = Frame(root)
leftFrame.place(x=50,y=100,width=300,height=650)

#cutie 
Logo_img = PhotoImage(file='student.png')
logo_Label = Label(leftFrame,image=Logo_img)
logo_Label.grid(row=0,column=0)


#Add Student Button
addstudentButton = ttk.Button(leftFrame,text='Add Student', width=20,state=DISABLED,command=add_student ) 
addstudentButton.grid(row=1,column=0,pady=20 )
#Search Student
searchstudentButton = ttk.Button(leftFrame,text='Search Student', width=20,state=DISABLED)
searchstudentButton.grid(row=2,column=0,pady=20 )
#Delete Student
delstudentButton = ttk.Button(leftFrame,text='Delete Student', width=20,state=DISABLED)
delstudentButton.grid(row=3,column=0,pady=20 )
#Update Student
updatestudentButton = ttk.Button(leftFrame,text='Update Student', width=20,state=DISABLED)
updatestudentButton.grid(row=4,column=0,pady=20 )
#Show Student
showstudentButton = ttk.Button(leftFrame,text='Show Student', width=20,state=DISABLED)
showstudentButton.grid(row=5,column=0,pady=20 )
#Export Data
exportdataButton = ttk.Button(leftFrame,text='Export Data', width=20,state=DISABLED)
exportdataButton.grid(row=6,column=0,pady=20 )
#EXIT
EXITButton = ttk.Button(leftFrame,text='EXIT', width=15)
EXITButton.grid(row=7,column=0,pady=50 )



#Right Portion
RightFrame = Frame(root)
RightFrame.place(x=330,y=120,width=830,height=630)


#Horizontal Scroll-Bar
scrollBarX = Scrollbar(RightFrame,orient=HORIZONTAL)      #orient to be horiental otherwise by default as vertical


#Vertical Scroll-Bar
scrollBarY = Scrollbar(RightFrame,orient=VERTICAL)



#MAIN TABLE AREA
main_table = ttk.Treeview(RightFrame,columns=('Name','ID','Mobile-No','Email','Address','Gender','Date-Of-Birth','Admission Year','Passing Year'),xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set )

#these configure the scroll bars into the main table 
scrollBarX.config(command=main_table.xview) 
scrollBarY.config(command=main_table.yview)



scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)


main_table.pack(fill=BOTH,expand=1)       #used to place when a complexity is less either bottom,top or etc

#Heading opf each columns in the main table 
main_table.heading('Name',text='NAME')
main_table.heading('ID',text='ID')
main_table.heading('Mobile-No',text='Mobile-No')
main_table.heading('Email',text='Email')
main_table.heading('Address',text='Address')
main_table.heading('Gender',text='Gender')
main_table.heading('Date-Of-Birth',text='Date-Of-Birth')
main_table.heading('Admission Year',text='Admission Year')
main_table.heading('Passing Year',text='Passing Year')

main_table.config(show='headings')






root.mainloop()