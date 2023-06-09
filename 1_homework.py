from tkinter import *
# from tkinter import ttk

window = Tk()
window.geometry("600x300")
window.title("REGISTRATION")
def save_butt():
    entry_lg_save = entry_lg.get()
    entry_pass_save = entry_pass.get
    with open("deveploment/logins_and_password.txt", "w") as f:
        f.write(f"Login: { entry_lg_save}, Password:{entry_pass_save}" )
        

label_name = Label(
    window,
    text="Login:",
    font=("Arial", 20, )
    )
label_name.place(x=70, y=30)

entry_lg  = Entry(
    window,
    textvariable="Login",
    width=30,
    font=40

)
entry_lg.place(x=70, y=80)

label_pass = Label(
    window,
    text="Password:",
    font=("Arial", 20)
)
label_pass.place(x=70, y=130)

entry_pass = Entry(
    window,
    width=30,
    font=40
)
entry_pass.place(x=70, y=180)
save_btt = Button(

    text="save",
    command=save_butt
)
save_btt.place(x=100, y=230)

window.mainloop()