from tkinter import *
from datetime import datetime as dt
from PIL import Image,ImageTk
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("655x333")
root.config(background ="dark red")

scrollbar = Scrollbar(root)
Scrollbar(root).pack(side= "right",fill =Y)

    
def click():
    tmsg.showinfo("Succesfull.","Thank you for submitting your information!!")
    print(f"{usernamevalue.get(), phonevalue.get(), emailvalue.get()}") 

    with open("records1.txt", "a") as f:
        f.write(f"{usernamevalue.get(), phonevalue.get(), emailvalue.get()}\n")

Label(root, text = "TIMES NOW", bg = "black", fg = "dark red", font = " lucida 16 bold", pady = 15, padx = 75, relief = SUNKEN).pack()
Label(root, text =f"Date : {dt.now().date()}", font = "lucida 10 bold", fg="black", bg="dark red").pack()

frame = Frame(root, borderwidth = 50, bg = "dark red", relief = SUNKEN)
frame.pack(side = LEFT, anchor = "nw", fill =Y)

l1 = Label(frame, text = "1.(A) Ashok Gehlot's Brother Summoned Today By Enforcement Directorate.\n1.(B) CBI Takes Over Search Of Haryana Girl,Two Years After She Went Missing.", font = "lucidia  16 bold", fg = "white", bg = "black", pady = 20)
l1.pack(pady = 5, padx = 5)


l2 = Label(frame, text = "2. 2020 Olympics postponed amid COVID-19 pandemic.", font = "lucida 16 bold", fg = "white", bg = "black", pady = 20)
l2.pack(pady = 5, padx = 5)

l3 = Label(frame, text = "3.(A) Delhi Professor Arrested In Bhima Koregaon Case Over 'Maoist Ideology' \n3.(B) The 19 dissident MLAs had filed a petition in the high court, challenging the disqualification notices.", font = "lucida 16 bold", fg = "white", bg = "black", pady = 20)
l3.pack(pady = 5, padx = 5)


username = Label(root, text = "Username")
phone = Label(root, text = "Phone")
email = Label(root, text = "Email-ID")

username.pack()
phone.pack()
email.pack()

usernamevalue = StringVar()
phonevalue = StringVar()
emailvalue = StringVar()

usernameentry = Entry(root, textvariable = usernamevalue)
phoneentry = Entry(root, textvariable = phonevalue)
emailentry = Entry(root, textvariable = emailvalue)

usernameentry.pack()
phoneentry.pack()
emailentry.pack()


Button(text = "Submit..", command = click).pack()


root.mainloop()