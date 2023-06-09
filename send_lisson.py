# from tkinter import *
# from tkinter import ttk
 
# root = Tk()
# root.title("METANIT.COM")
# root.geometry("250x200")
 
# # стандартная кнопка
# btn = ttk.Button(text="Button")
# btn.pack(fill="x")
 
# root.mainloop()
# from tkinter import *

# root = Tk()
# btn1 = Button(root, text="Button 1", fg="red", bg="yellow")
# btn2 = Button(root, text="Button 2", fg="orange", bg="green")
# btn3 = Button(root, text="Button 3", fg="white", bg="blue")
# btn1.pack(side=LEFT)
# btn2.pack(side=LEFT)
# btn3.pack(side=RIGHT)
# root.mainloop()



# from tkinter import *

# window = Tk()
# window.title("Welcome to grid app!")
# lbl = Label(window, text="Hello!")
# btn1 = Button(window, text="Click Me!")
# btn2 = Button(window, text="Click Me!")
# btn3 = Button(window, text="Click Me!")
# btn1.grid(column=0, row=0)
# lbl.grid(column=1, row=0)
# btn2.grid(column=2, row=0, rowspan=2)
# btn3.grid(column=1, row=1)
# window.mainloop()


# from tkinter import *

# root = Tk()
# root.title("Welcome to the second entry app")

# root.geometry("925x500+300+200")
# frame = Frame(root, width=350, height=350, bg="red").place(x=480, y=50)

# frame2 = Frame(root, width=350, height=350, bg="blue").place(x=50, y=50)

# lbl_login = Label(frame, text="Login")
# lbl_login.place(x=100, y=100)
# lbl_pass = Label(root, text="Password")

# txt1 = Entry(root, width=10)
# txt2 = Entry(root, width=10)

# btn = Button(root, text="Enter")

# # lbl_login.grid(row=0, sticky=E)
# lbl_pass.grid(row=1, sticky=E)
# txt1.grid(row=0, column=1)
# txt2.grid(row=1, column=1)
# btn.grid(columnspan=2, sticky=NSEW)
# root.mainloop()




from tkinter import *
from tkinter import messagebox


def display_full_name():
    messagebox.showinfo("GUI Python", name.get() + " " + surname.get())

root = Tk()
root.title("GUI на Python")

name = StringVar()
surname = StringVar()

name_label = Label(text="Введите имя:")
surname_label = Label(text="Введите фамилию:")

name_label.grid(row=0, column=0, sticky="w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entry = Entry(textvariable=surname)

name_entry.grid(row=0,column=1, padx=5, pady=5)
surname_entry.grid(row=1,column=1, padx=5, pady=5)


message_button = Button(text="Click Me", command=display_full_name)
message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")

root.mainloop()