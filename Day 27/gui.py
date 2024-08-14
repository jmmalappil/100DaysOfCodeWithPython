from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

def button_clicked():
    if input.get() != " ":
        text = input.get()
        my_label["text"] = text

#Label
my_label = Label(text="I am a Label",font=("Arial",24, "bold"))
my_label.grid(row=0,column=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1,column=1)

button1 = Button(text="High Five")
button1.grid(row=0,column=2)

#Entry

input = Entry()
input.grid(row=2,column=3)



window.mainloop()