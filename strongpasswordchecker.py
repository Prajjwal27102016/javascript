import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = password_entry.get()
    length = len(password)
    
    if length == 0:
        result_label.config(text="Please enter a password", fg="black")
    elif length < 6:
        result_label.config(text="Strength: Weak", fg="red")
    elif length <= 10:
        result_label.config(text="Strength: Medium", fg="orange")
    else:
        result_label.config(text="Strength: Strong", fg="green")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

# Add a title label
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Password input field (show="*" hides the actual characters)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

# Button to trigger the check
check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 11, "bold"))
result_label.pack(pady=5)

# Start the application
root.mainloop()