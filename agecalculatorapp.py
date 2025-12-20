import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        
        today = date.today()
        birth_date = date(year, month, day)
        
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        result_label.config(text=f"Your Age is: {age} years", fg="green")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x350")

tk.Label(root, text="Age Calculator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter Day (DD):").pack()
day_entry = tk.Entry(root)
day_entry.pack(pady=5)

tk.Label(root, text="Enter Month (MM):").pack()
month_entry = tk.Entry(root)
month_entry.pack(pady=5)

tk.Label(root, text="Enter Year (YYYY):").pack()
year_entry = tk.Entry(root)
year_entry.pack(pady=5)

calc_button = tk.Button(root, text="Calculate Age", command=calculate_age, bg="blue", fg="white")
calc_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()