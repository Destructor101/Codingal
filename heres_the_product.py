from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Getting Started With Widgets")

lbl1 = Label(root, fg="black", bg="white", text="Multiply Two Numbers")
lbl1.pack(side="top", fill="x")

input_frame = Frame(master=root, height = 150, width = 360, bg="#d0efff")
input_frame.pack(padx = 20)

lbl2 = Label(input_frame, text="Enter first number:", fg="white", bg="#3895D3", width=17)
lbl2.place(x=20, y=25)
lbl3 = Label(input_frame, text="Enter second number:", fg="white", bg="#3895D3",width=17)
lbl3.place(x=20, y=85)

first_number = Entry(input_frame)
second_number = Entry(input_frame)
first_number.place(x = 180, y = 25)
second_number.place(x = 180, y = 85)

def display():
    product = float(first_number.get())*float(second_number.get())
    textbox.insert(END, "The product is ")
    textbox.insert(END, product)

textbox = textbox = Text(bg="#BEBEBE", fg="black")

btn = Button(text="Multiply", bg="#3895D3", command=display, pady=10)
btn.pack(pady=5)
textbox.pack(pady=5)

root.mainloop()
