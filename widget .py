from tkinter import *
from datetime import date

root= Tk()
root.title("WIDGETS")
root.geometry("500x500")

p = Label(text= "hey there",fg="blue",bg="#38FFF8",font=("Arial",24,"bold"),height=1,width=300)

name_p = Label(text=" Full Name", bg="#FC68F0")
name_entry = Entry()

def display():
    name = name_entry.get()
    
    global message
    greet = "Hello" + name +"\n "
    message= "welcome to the Application! \nTodays date is :"
    
    text_box.insert(END,greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="Bergin", command= display,height=1, bg="#45F0D3",fg="purple")
 
p.pack()
name_p.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()