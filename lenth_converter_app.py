import tkinter as tk
from tkinter import messagebox

def convert_to_cm():
    try:
        inches = float(entry_inches.get())
        cm = inches * 2.54
        label_result.config(text=f"Result: {cm:.2f} cm", fg="blue")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric value.")

root = tk.Tk()
root.title("Inches to CM Converter")
root.geometry("300x200")

tk.Label(root, text="Enter length in inches:", font=("Arial", 10)).pack(pady=10)

entry_inches = tk.Entry(root)
entry_inches.pack(pady=5)

btn_convert = tk.Button(root, text="Convert", command=convert_to_cm)
btn_convert.pack(pady=10)

label_result = tk.Label(root, text="Result: 0.00 cm", font=("Arial", 12, "bold"))
label_result.pack(pady=10)

root.mainloop()