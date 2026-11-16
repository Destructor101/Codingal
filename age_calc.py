from tkinter import *
from datetime import date

window = Tk()
window.geometry("400x400")
window.title("Age Calculator App")

title = Label(text="Age Calculator", fg="white", bg="#064975")
title.pack(fill=X)

entry_frame = Frame(master=window, height=240, width=300, bg="#d0efff")
entry_frame.pack()

name_lbl = Label(entry_frame, text="Enter Name:", bg="#3895D3")
date_lbl = Label(entry_frame, text="Enter Date:", bg="#3895D3")
month_lbl = Label(entry_frame, text="Enter Month:", bg="#3895D3")
year_lbl = Label(entry_frame, text="Enter Year:", bg="#3895D3")

name_entry = Entry(entry_frame, width=12, bg="#DFDBDB")
date_entry = Entry(entry_frame, width=12, bg="#DFDBDB")
month_entry = Entry(entry_frame, width=12, bg="#DFDBDB")
year_entry = Entry(entry_frame, width=12, bg="#DFDBDB")

name_lbl.place(x=40, y=20)
date_lbl.place(x=40, y=80)
month_lbl.place(x=40, y=140)
year_lbl.place(x=40, y=200)

name_entry.place(x=190, y=20)
date_entry.place(x=190, y=80)
month_entry.place(x=190, y=140)
year_entry.place(x=190, y=200)

textbox = Text(window, height=50, width=400)

def display():
    name = name_entry.get()
    given_date = int(date_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())
    today = date.today()
    today_year, today_month, today_date = today.year, today.month, today.day

    years = today_year-year
    if today_month < month:
        years -= 1
        months = 12 - month + today_month
    else:
        months = today_month - month
    if today_date < given_date:
        months -= 1
        days = 30 - given_date + today_date
    else:
        days = today_date - given_date

    textbox.insert(END, f"Hello {name}!\n")
    textbox.insert(END, f"You are {years} years, {months} and {days} days old!")
    

enter_button = Button(text="Find Age", command=display, bg="#064975", fg="white")
enter_button.pack(pady=5)   

textbox.pack()


window.mainloop()