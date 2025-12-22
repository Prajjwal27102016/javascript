from tkinter import *


# Create window
window = Tk()
window.title("Event Handler")
window.geometry("500x500")


# Event Handler for Keypress
def handle_keypress(event):
   #Print the character associated to the key pressed
   print(event.char)


# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)


# Event handler for button click
def handle_clickL(event):
   print("\nI did a left click!")
def handle_clickR(event):
   print("\nI did a right click!")
def handle_click_wheel(event):
   print("\nI am using wheel!")
button = Button(text="Click me!")
button.pack()


# Bind click event to handle_click()
button.bind("<Button-1>", handle_clickL)
button.bind("<Button-3>", handle_clickR)


button.bind("<Button-2>", handle_click_wheel)
window.mainloop()