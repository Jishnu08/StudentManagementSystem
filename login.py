from tkinter import *       #tkinder is a file having all GUI objects and classes
from tkinter import messagebox
from PIL import ImageTk

def login():
    if username_entry.get()=='' or  pswd_entry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif username_entry.get()=='jishnu' and pswd_entry.get()=='2003':
        messagebox.showinfo('Success','Welcome to the System')
        window.destroy()
        import main






    else:
        messagebox.showerror('ERROR', 'Please Show Correct Credentials')
        
         








window=Tk()            #to create the window
window.title('Login System')
window.geometry('1000x650+265+100')          #used to set the window dimensions ('L x B + X-axis + Y-axis')
window.resizable(False,False)               #used to pass false for window maximise button which disables the maximise button


#importing the background image
background_img = ImageTk.PhotoImage(file='bg.jpg')

#using a label function which helps to indicate where the picture is going to be placed 
background_label = Label(window,image=background_img)
background_label.place(x=0,y=0)

#Frame is to make a container like box inside the window
login_frame = Frame(window, bg='white')
#login_frame.attribute('-transparentcolor', '#ab23ff')
login_frame.place(x=300,y=150)

#userDp image
logo_img = PhotoImage(file='login_DP.png')          #importing png pic no need of ImageTk as its png
Logo_label = Label(login_frame,image=logo_img , bg='white')
Logo_label.grid (row=0,column=0,columnspan=3,pady=10)



#Username login portion
username_img = PhotoImage(file='user.png')
username_label = Label(login_frame,image=username_img ,text='Username', compound=LEFT, font=('times new roman',15,'bold'), bg='white')
username_label.grid(row=1,column=0, pady = 10,padx=20)

#username entry field
username_entry = Entry(login_frame, font=('times new roman',15,'bold'), fg = 'Red')
username_entry.grid (row=1,column=2,padx=10,pady=20)



#password login portion 
pswd_img = PhotoImage(file='Password.png')
pswd_label = Label(login_frame,image=pswd_img ,text='Password', compound=LEFT, font=('times new roman',15,'bold'), bg='white')
pswd_label.grid(row=2,column=0,pady=10, padx=20)


#passwod entry field 
pswd_entry = Entry(login_frame, font=('times new roman',15,'bold'), fg = 'Red')
pswd_entry.grid (row=2,column=2,pady = 10, padx = 20)



#Login Button
LoginButton = Button(login_frame,text='Login', font=('times new roman',13,'bold'), width=12, bg='green', fg='yellow', activebackground='deeppink', activeforeground='green', cursor='hand1', command=login)
LoginButton.grid(row=3,column=2,padx=20, pady=10)







window.mainloop()          #keeps the window continously  visible 




