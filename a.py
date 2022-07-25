from tkinter import *
from tkinter import ttk
import csv


def login():
    email = mail.get()
    password = pwd.get()
    Mobileno = mobile.get()
    Accountno = accno.get()
    IFSCcode = ifsc.get()
    if email == '' and password == '':
        message.set('fill the columns')
    else:
        f = open('E:\\Book.csv', 'r')
        g = csv.reader(f)
        found = False
        for row in g:
            if email == row[0] and password == row[1]:
                found = True

        if found == True:
            message.set('Login success')
            button = Button(window,text = 'Next',fg ='black',bg = 'green',command = new_window,width=8,height=1).place(x=500,y=150)
        else:
            message.set('wrong')


window = Tk()
window.title('Login Form')
window.geometry('600x400')
window.configure(background='light blue')
mail = StringVar()
pwd = StringVar()
message = StringVar()
mobile = IntVar()
accno = IntVar()
ifsc = IntVar()

Label(window, text='Please fill the following details', bg='red', font=('Times', 17)).pack()

Label(window, text='Username', bg='light blue', font=('Times', 15)).place(x=140, y=60)
Label(window, text=':', fg='black', bg='light blue', font=('Broadway')).place(x=230, y=60)
Entry(window, textvariable=mail, font=('Times', 14)).place(x=250, y=60)

Label(window, text='Password', bg='light blue', font=('Times', 15)).place(x=140, y=100)
Label(window, text=':', fg='black', bg='light blue', font=('Broadway')).place(x=230, y=100)
Entry(window, textvariable=pwd, show='*', font=('Times', 14)).place(x=250, y=100)

Label(window, text='', textvariable=message, bg='light blue').place(x=250, y=200)

Button(window, text="Login", width=10, height=1, command=login, bg='light blue').place(x=250, y=150)


def new_window():
    newWindow = Tk()
    newWindow.title('Details')
    newWindow.geometry('800x500')
    newWindow.configure(background='light blue')
    name = StringVar()
    Label(newWindow, text='Enter your Details', fg='black', bg='red', font=("Monotype Corsiva", 25), width=80).pack()

    Label(newWindow, text='Name', font=('Maiandra GD', 14), bg='light blue').place(x=10, y=60)
    Label(newWindow, text=':', fg='black', bg='light blue', font=('Elephant')).place(x=180, y=60)
    Name = Entry(newWindow, textvariable=name, font=('Maiandra GD', 13))
    Name.place(x=200, y=60)

    Label(newWindow, text='Occupation', font=('Maiandra GD', 14), bg='light blue').place(x=10, y=100)
    Label(newWindow, text=':', fg='black', bg='light blue', font=('Elephant')).place(x=180, y=100)
    course = ('Evaluator', 'Coordinator', 'Assistant Head Examiner', 'Head Examiner')
    combo = ttk.Combobox(newWindow, value=course, width=20, height=4, font=('Maiandra GD', 13)).place(x=200, y=100)

    mobileNumber = Label(newWindow, text='Mobile number', font=('Maiandra GD', 14), bg='light blue')
    mobileNumber.place(x=10, y=140)
    Label(newWindow, text=':', fg='black', bg='light blue', font=('Elephant')).place(x=180, y=140)
    Entry(newWindow, textvariable=mobile, font=('Maiandra GD', 13)).place(x=200, y=140)

    Label(newWindow, text='Account number', font=('Maiandra GD', 14), bg='light blue').place(x=10, y=180)
    Label(newWindow, text=':', fg='black', bg='light blue', font=('Elephant')).place(x=180, y=180)
    Entry(newWindow, textvariable=accno, font=('Maiandra GD', 13)).place(x=200, y=180)

    Label(newWindow, text='IFSC code', font=('Maiandra GD', 14), bg='light blue').place(x=10, y=220)
    Label(newWindow, text=':', fg='black', bg='light blue', font=('Elephant')).place(x=180, y=220)
    Entry(newWindow, textvariable=ifsc, font=('Maiandra GD', 13)).place(x=200, y=220)
    messageLabel = Label(newWindow, text='', bg='light blue')
    messageLabel.place(x=400, y=300)
    Button(newWindow, text="Check", width=10, height=1, command=lambda: check(Name.get(), messageLabel),
           bg='light blue').place(x=500, y=250)


def check(Name, messageLabel):
    if Name == '':
        messageLabel.config(text='Enter name')

    else:
        f = open('E://Book.csv', 'r')
        g = csv.reader(f)
        found = False
        for row in g:
            if Name == row[2]:
                found = True
        if found == True:
            messageLabel.config(text='Correct name')
        else:
            messageLabel.config(text='Wrong name')

mainloop()
