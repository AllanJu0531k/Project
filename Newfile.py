from tkinter import *
from tkinter import ttk
import csv


window = Tk()
window.title('CBSE')
window.geometry('500x300')
window.configure(background='Lavender')

Label(window, text='CBSE', fg='black', bg='red', font=("Monotype Corsiva", 25), width=80).pack()
Label(window, text='CBSE Form', fg='black', bg='lavender', font=("Times", 25), width=80).pack()
Button(window, text="Staff", width=10, height=1, bg='light blue', font=("Maiandra GD", 20),command=staff).place(x=160,y=100)
Button(window, text="Student", width=10, height=1, bg='light blue', font=("Maiandra GD", 20)).place(x=160,y=190)



def staff():
    newWindow = Tk()
    newWindow.title('Details')
    newWindow.geometry('600x400')
    newWindow.configure(background='light blue')
    mail = StringVar()
    pwd = StringVar()
    window.destroy()
    
    Label(newWindow,text='Please fill the following details', bg='red', font=('Times', 17)).pack()

    Label(newWindow, text='Username', bg='light blue', font=('Times', 15)).place(x=140, y=60)
    Label(newWindow, text=':', fg='black', bg='light blue', font=('Broadway')).place(x=230, y=60)
    Mail = Entry(newWindow, textvariable=mail, font=('Times', 14))
    Mail.place(x=250, y=60)

    Label(newWindow, text='Password', bg='light blue', font=('Times', 15)).place(x=140, y=100)
    Label(newWindow, text=':', fg='black', bg='light blue', font=('Broadway')).place(x=230, y=100)
    Pwd = Entry(newWindow, textvariable=pwd, show='*', font=('Times', 14))
    Pwd.place(x=250, y=100)

    mess = Label(newWindow, text='', bg='light blue')
    mess.place(x=250, y=200)
    
    Button(newWindow, text="login", width=10, height=1,command=lambda:login(Mail.get(),Pwd.get(),mess), bg='light blue',).place(x=250, y=150)
    
    
def login(Mail,Pwd,mess):
    if Mail == '' and Pwd == '':
        mess.config(text='Enter')
        
    else:
        f = open('E:\\Book.csv', 'r')
        g = csv.reader(f)
        found = False
        for row in g:
            if Mail == row[0] and Pwd == row[1]:
                found = True

        if found == True:
            mess.config(text='Correct')
        else:
            mess.config(text='Wrong')
            
            
            
mainloop()
