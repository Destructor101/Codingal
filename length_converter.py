from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")
root.title("Length Converter App")

frame = Frame(height=80, width=300, bg="#B6DCF5", relief="ridge",border=1)
frame.pack(padx=50, pady=20)

lbl = Label(frame, text="Enter Length in inches", bg="#3895D3", fg="white")
lbl.place(x=10, y=10)

entry = Entry(frame, width=10, bg="#DFDBDB")
entry.place(x=200, y=10)

def convert():
    textbox.delete("1.0",END)
    try:
        length = float(entry.get())
    except ValueError:
        messagebox.showerror(title="Invalid input", message="Please enter a valid number")

    textbox.insert(END, f"Entered value: {length} inches\nConverted Value: {length*2.54:.2f} cm")

textbox = Text(bg="#D4D2D2", font=("Arial", 15))
textbox.pack(pady=20, fill="x")

btn = Button(frame, bg="#3895D3", text="Convert", fg="white", command=convert)
btn.place(relx=0.5, rely=0.7, anchor=CENTER)


root.mainloop()
