from tkinter import *

def convert():
    miles_num = float(Miles.get())
    km_num = round(miles_num * 1.609, 2)
    km_str = str(km_num)
    km.config(text=km_str)

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=500,height=300)
window.config(padx=20, pady=20)

#Miles Input

Miles = Entry(width=7)
Miles.grid(row=0,column=1)

miles_text = Label(text="Miles")
miles_text.grid(row=0,column=2)

equal_text = Label(text="is equal to")
equal_text.grid(row=1,column=0)

km = Label(text="0")
km.grid(row=1,column=1)

km_text = Label(text="Km")
km_text.grid(row=1,column=2)

# Button

button = Button(text="Calculate",command=convert)
button.grid(row=2,column=1)





window.mainloop()