from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.geometry("400x400")
window.title("Rock Paper Scisors")

head_lbl = Label(text="Let's Play Rock-Paper-Scissors! Make your choice!", font=("Arial", 10, "bold"), bg="lightblue", fg="white")

choice = StringVar(value="Pick Your Choice!")

choice_lbl = Label(text=f"You Chose: {choice.get()}", bg="white", fg="black")

button_frame = Frame(master=window, width="300", height="50")
rock_button = Button(master=button_frame,text="Pick Rock", command=lambda: [choice.set("Rock"), choice_lbl.config(text="You Chose: Rock")], bg="lightgray", width=10)
paper_button = Button(master=button_frame,text="Pick Paper", command=lambda: [choice.set("Paper"), choice_lbl.config(text="You Chose: Paper")], bg="lightgray", width=10)
scissors_button = Button(master=button_frame,text="Pick Scissors", command=lambda: [choice.set("Scissors"), choice_lbl.config(text="You Chose: Scissors")], bg="lightgray", width=10)

def play():
    cpu_choice = random.choice(["Rock", "Paper", "Scissors"])
    win = ""
    if cpu_choice == choice.get():
        win = "draw"
    else:
        match choice.get():
            case "Rock": win = "win" if cpu_choice == "Scissors" else "lose"
            case "Paper": win = "win" if cpu_choice == "Rock" else "lose"
            case "Scissors": win = "win" if cpu_choice == "Paper" else "lose"

    match win:
        case "win": messagebox.showinfo("Game Result", f"YOU WIN! :)\nBot chose {cpu_choice}",)
        case "lose": messagebox.showinfo("Game Result", f"YOU LOST! :(\nBot chose {cpu_choice}")
        case "draw": messagebox.showinfo("Game Result", f"ITS A DRAW! ~_~\nBot chose {cpu_choice}")
        case _: messagebox.showerror("Choice not selected!", "Please select a choice using the buttons")


lock_button = Button(text="LOCK IN", bg="gray", fg="black", command=play)

head_lbl.pack(fill=X)
choice_lbl.pack(anchor=CENTER, pady=10)

button_frame.pack(pady=20, anchor=CENTER)

rock_button.place(x=0, y=0)
paper_button.place(x=105, y=0)
scissors_button.place(x=210, y=0)

lock_button.pack(pady=10, anchor=CENTER)

window.mainloop()