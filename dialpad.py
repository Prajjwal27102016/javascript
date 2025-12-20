from tkinter import *


# --- Window Setup ---
root = Tk()
root.title('Simple Number Pad')
root.geometry('250x350') # Slightly adjusted size


# --- Display Area ---
current_input = StringVar()
display = Entry(root, textvariable=current_input, font=('Arial', 20), bd=3, relief=SUNKEN, justify='right')
display.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)


# --- Button Data ---
# Numbers and operations layout
buttons = [
   ('9', 1, 0), ('8', 1, 1), ('7', 1, 2),
   ('6', 2, 0), ('5', 2, 1), ('4', 2, 2),
   ('3', 3, 0), ('2', 3, 1), ('1', 3, 2),
   ('C', 4, 0), ('0', 4, 1), ('DEL', 4, 2)
]




# --- Button Click Handler ---
def button_click(char):
   """Handles button presses to update the display."""
   current_text = current_input.get()
   if char == 'C': # Clear
       current_input.set("")
   elif char == 'DEL': # Delete last character
       current_input.set(current_text[:-1])
   else: # Append character
       current_input.set(current_text + char)


# --- Configure Grid Resizing ---
# Ensure columns and rows expand proportionally
for i in range(3): # For 3 columns
   root.columnconfigure(i, weight=1)
for i in range(5): # For 5 rows (1 display row + 4 button rows)
   root.rowconfigure(i, weight=1)


# --- Create and Place Buttons ---
for (text, r, c) in buttons:
   btn = Button(root, text=text, font=('Arial', 18, 'bold'), bg='#e0f2f7',
                command=lambda char=text: button_click(char))
   btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)


# --- Start the GUI Loop ---
root.mainloop()

