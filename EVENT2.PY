# Import necessary libraries
from tkinter import *
from tkinter import messagebox


# Setup Tkinter Window
root = Tk()
root.geometry("200x200")
root.title("Virus Scanner")




def msg():
   messagebox.showinfo("Success ", "Virus not at all found!")


# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)


# Entering main event loop
root.mainloop()

